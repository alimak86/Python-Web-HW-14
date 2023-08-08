from typing import List, Union

from sqlalchemy.orm import Session, subqueryload
from src.database.models import Contact, User
from src.schemas import ContactModel, ResponseContactModel
from abc import abstractmethod
from sqlalchemy import and_


class BaseContact:
"""
clas BaseContact is a base class for the rest of the contact classes. It is common part

: db : Session
: user : User
"""
  def __init__(self, db: Session, user: User):
    self.db = db
    self.user = user

  @abstractmethod
  async def __call__(self):
    pass


class Get_Contacts(BaseContact):
"""
class Get_Contacts is responsible for the acquiring of the list of contacts

: skip : int
: limit : int
: __call__() -> List[Contact]
"""
  def __init__(self, skip:int, limit:int, db: Session, user: User):
    super().__init__(db, user)
    self.skip = skip
    self.limit = limit

  async def __call__(self) -> List[Contact]:
    return self.db.query(Contact).filter(
      Contact.user_id == self.user.id).offset(self.skip).limit(
        self.limit).all()


class Create_Contact(BaseContact):
"""
class Create_Contact is responsible to create a Contact

: body : body request
: db : Session
: user : User
: __call__() - > Contact
"""
  def __init__(self, body, db, user):
    super().__init__(db, user)
    self.body = body

  async def __call__(self) -> Contact:
    new_contact = Contact(
      user_id=self.user.id,
      firstname=self.body.firstname,
      secondname=self.body.secondname,
      email=self.body.email,
      phonenumber=self.body.phonenumber,
      dateofbirth=self.body.dateofbirth,
    )
    self.db.add(new_contact)
    self.db.commit()
    self.db.refresh(new_contact)
    return new_contact


class Get_Contact(BaseContact):
"""
class Get_Contact is responsible to get a Contact

: db : Session
: contac_id : int
: user : User
: __call__() -> Contact
"""
  def __init__(self, contact_id, db, user):
    super().__init__(db, user)
    self.contact_id = contact_id

  async def __call__(self) -> Contact:
    return self.db.query(Contact).filter(
      and_(Contact.id == self.contact_id,
           Contact.user_id == self.user.id)).first()


class Get_Contact_by_Name(BaseContact):
"""
class Get_Contatc_by_Name is responsible to get a contatc by name

: contact_name : str
: db : Session
: user : User
"""
  def __init__(self, contact_name: str, db: Session, user: User):
    super().__init__(db, user)
    self.contact_name = contact_name

  async def __call__(self) -> Contact:
    return self.db.query(Contact).filter(
      and_(Contact.firstname == self.contact_name,
           Contact.user_id == self.user.id)).all()


class Get_Contact_by_Second_Name(BaseContact):
"""
class Get_Contatc_by_Second_Name is responsible to get a contatc by second name

: contact_name : str
: db : Session
: user : User
"""

  def __init__(self, contact_name: str, db: Session, user: User):
    super().__init__(db, user)
    self.contact_name = contact_name

  async def __call__(self) -> Contact:
    return self.db.query(Contact).filter(
      and_(Contact.secondname == self.contact_name,
           Contact.user_id == self.user.id)).all()


class Get_Contact_by_Email(BaseContact):
"""
class Get_Contatc_by_Email is responsible to get a contatc by email

: email : str
: db : Session
: user : User
"""

  def __init__(self, email: str, db: Session, user: User):
    super().__init__(db, user)
    self.email = email

  async def __call__(self) -> Contact:
    return self.db.query(Contact).filter(
      and_(Contact.email == self.email,
           Contact.user_id == self.user.id)).all()


class Update_Contact(BaseContact):
"""
class Update_Contact is responsible for the contatc info updates

: contact_id : int
: body : body request
: db :  Session
: user : User
"""
  def __init__(self, contact_id, body, db, user):
    super().__init__(db, user)
    self.contact_id = contact_id
    self.body = body

  async def __call__(self) -> Union[Contact, None]:
    contact = self.db.query(Contact).filter(
      and_(Contact.id == self.contact_id,
           Contact.user_id == self.user.id)).first()
    if contact:
      contact.user_id = self.user.id,
      contact.firstname = self.body.firstname,
      contact.secondname = self.body.secondname,
      contact.email = self.body.email,
      contact.phonenumber = self.body.phonenumber,
      contact.dateofbirth = self.body.dateofbirth,
      self.db.commit()
    return contact


class Remove_Contact(BaseContact):
"""
class Remove_Contact

: conact_id : int
: db : Session
: user : User
"""
  def __init__(self, contact_id, db, user):
    super().__init__(db, user)
    self.contact_id = contact_id

  async def __call__(self) -> Union[Contact, None]:
    contact = self.db.query(Contact).filter(
      and_(Contact.id == self.contact_id,
           Contact.user_id == self.user.id)).first()
    if contact:
      self.db.delete(contact)
      self.db.commit()
    return contact
