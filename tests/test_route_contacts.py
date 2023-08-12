from unittest.mock import MagicMock, patch

import pytest

from src.database.models import User
from src.services.auth import auth_service

@pytest.fixture()
def token(client, user, session, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    client.post("/api/auth/signup", json=user)
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    return data["access_token"]

def test_create_contact(client,token):
    # with patch.object(auth_service, 'r') as r_mock:
    #     r_mock.get.return_value = None
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
