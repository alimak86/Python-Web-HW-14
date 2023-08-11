import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel,ContactModelFullName,ResponseContactModel,UserDb,UserModel,UserResponse,RequestEmail
from src.repository.contacts import Get_Contact, Get_Contact_by_Name, Remove_Contact

import random
from faker import Faker

NUMBER_OF_PERSONS = 100
class Random_Name:
    def __init__(self):
        fake = Faker()
        firstname,secondname = fake.name().split()
        self.firstname = firstname
        self.secondname = secondname

class List_Generator:
    def __init__(self, max_amount):
        ## random number of contacts
        ## with random name
        self.amount = random.randrange(1,max_amount)
        self.name = Random_Name()
        ##print(f"first: {self.name.firstname} second:{self.name.secondname}")

    def get_list_of_contacts(self):
        list_contacts = []
        for num in range(self.amount):
            contact = Contact(firstname = self.name)
            list_contacts.append(contact)

        return self.name.firstname, list_contacts


class Test_Repository_Contacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        ###print("initialize test:")
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_found_contact(self):
        contact_id = 1
        contact = Contact(id = contact_id)
        self.session.query().filter().first.return_value = contact
        execute = Get_Contact(contact_id, self.session, self.user)
        test_contact = await execute()
        self.assertEqual(contact, test_contact)

    async def test_not_found_contact(self):
        contact_id = 1
        # contact = Contact(id = contact_id)
        self.session.query().filter().first.return_value = None
        execute = Get_Contact(contact_id, self.session, self.user)
        test_contact = await execute()
        self.assertIsNone(test_contact)        

    async def test_found_contact_by_name(self):
        ## generate list of contacts with the firstname equal name (default = alisa)
        name, list_contacts = List_Generator(NUMBER_OF_PERSONS).get_list_of_contacts() 
        self.session.query().filter().all.return_value = list_contacts
        execute = Get_Contact_by_Name(name, self.session, self.user)
        contacts = await execute()
        ###print(f"found: {len(contacts)}")
        self.assertEqual(contacts, list_contacts)

    async def test_not_found_contact_by_name(self):
        ## generate list of contacts with the firstname equal name (default = alisa)
        name, list_contacts = List_Generator(NUMBER_OF_PERSONS).get_list_of_contacts() 
        self.session.query().filter().all.return_value = None
        execute = Get_Contact_by_Name(name, self.session, self.user)
        contacts = await execute()
        # print(f"not found: {len(contacts)}")
        self.assertEqual(contacts,None)

    async def test_remove_contact(self):
        contact_id = 1
        contact = Contact(id = contact_id)
        self.session.query().filter().first.return_value = contact
        execute = Remove_Contact(contact_id, self.session, self.user)
        test_contact = await execute()
        self.assertEqual(contact, test_contact)

    async def test_remove_contact_not_found(self):
        contact_id = 1
        self.session.query().filter().first.return_value = None
        execute = Remove_Contact(contact_id, self.session, self.user)
        test_contact = await execute()
        self.assertIsNone(test_contact)

if __name__ == '__main__':
    unittest.main()