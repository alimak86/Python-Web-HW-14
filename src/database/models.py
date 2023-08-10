from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from src.database.database import Connect_db, SQLALCHEMY_DATABASE_URL_FOR_WORK

Base = declarative_base()
Base.metadata.create_all(Connect_db(SQLALCHEMY_DATABASE_URL_FOR_WORK).engine)


class Contact(Base):
  """
  Sqlalchemy class Contact for the database of the contacts

  :param id: id of the contact
  :type id: int
  :param firstname: first name of the contact
  :type firstname: str
  :param secondname: second name of the contact
  :type secondname: str
  :param email: email of the contact
  :type email: str
  :param phonenumber: phone number of the contact
  :type phonenumber: str
  :param dateofbirth: date of birth of the contact
  :type dateofbirth: str
  :param user_id: id of the authorized user 
  :param user: is used for the connection with the table User
  """
  __tablename__ = "contacts"
  id = Column(Integer, primary_key=True)
  firstname = Column(String(50), nullable=False)
  secondname = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  phonenumber = Column(String(50), nullable=False)
  dateofbirth = Column(String(50), nullable=False)
  user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
  user = relationship('User', backref="contacts")  

class User(Base):
  """
  Sqlalchemy class User for the database of the authorized users

  :param id: id of the user
  :type id: int
  :param username:
  :type username: str
  :param email:
  :type email: str
  :param password: 
  :type password: str
  :param created_at: phone number of the contact
  :type created_at: datetime
  :param avatar: date of birth of the contact
  :type avatar: str
  :param refresh_token: token for the authorized user
  :param confirmed: True if user is authorized
  """

  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  username = Column(String(50))
  email = Column(String(250), nullable=False, unique=True)
  password = Column(String(255), nullable=False)
  created_at = Column('crated_at', DateTime, default=func.now())
  avatar = Column(String(255), nullable=True)
  refresh_token = Column(String(255), nullable=True)
  confirmed = Column(Boolean, default = False)
