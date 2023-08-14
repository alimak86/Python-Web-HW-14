from unittest.mock import MagicMock, patch

import pytest

from src.database.models import User
from src.services.auth import auth_service
from src.services.email import email_service

from src.database.database import Connect_db,SQLALCHEMY_DATABASE_URL_FOR_WORK
from sqlalchemy.orm import Session
from fastapi import Depends

## use it because other db does not work
get_db = Connect_db(SQLALCHEMY_DATABASE_URL_FOR_WORK).session()
#
@pytest.fixture()
def token(client, user, monkeypatch, session: Session = get_db):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.services.email.email_service.send_email", mock_send_email)
    response = client.post("/api/auth/signup", json=user)

######648237462184762184762486234826348234
    # dat = response.json()
    # print(dat)
    # print(user.get("email"))
    # print(user.get("password"))
#$%%%%%%%%%%%%%%%%%%%%%%%%%############################

    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()

#@#$@$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # all_users =  session.query(User).all()
    # print(all_users)
###0967064-0643-6435643653456453634543

    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    print(data)

#    data = {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZWFkcG9vbDJAZXhhbXBsZS5jb20iLCJpYXQiOjE2OTE5ODQxNjQsImV4cCI6MTY5MTk4NTA2NCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4ifQ.iS1XCNXlHz2TFHwPK47QkqKQmIvUppXogbIwvISIwpw"}
    return data["access_token"]

def test_root(client):
    response = client.get("/")
    data = response.json()
    assert data["message"] == "Welcome to Contact Book"

def test_login_user(client, user, session: Session = get_db):
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"
   
def test_create_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
    response = client.post("api/contacts", json = {"firstname":"alisa"}, headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["firstname"] == "alisa"

def test_get_contacts(client,token):
    response = client.get("api/contacts", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data,list)

def test_get_contact(client,token):
    response = client.get("api/contacts/1", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["firstname"] == "alisa"

def test_get_contact_not_found(client,token):
    response = client.get("api/contacts/2", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"

def test_get_contact_by_name(client,token):
    response = client.get("api/contacts/alisa", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data,list)
    assert data[0]["firstname"] == "alisa"

def test_get_contact_by_name_not_found(client,token):
    response = client.get("api/contacts/nikita", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"

def test_remove_contact(client,token):
    response = client.delete("api/contacts/1", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["firstname"] == "alisa"
    assert data["id"] == 1

def test_remove_contact_not_found(client,token):
    response = client.delete("api/contacts/1", headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"
