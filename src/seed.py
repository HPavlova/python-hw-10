from email import message
from logging import warning
from bson import ObjectId
from faker import Faker
fake = Faker()
from mongoengine import DoesNotExist

from src.lru_cache import cache, LruCache
from src.models import Contact



def generate_fake_contacts():
    for i in range(20):
        fake_contact = Contact(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        phone = fake.phone_number(),
        email = fake.email())
    fake_contact.save()

def add_phone(contact_id, phone):
    contact = Contact.__objects.get(id=ObjectId(contact_id))
    contact.phone.append(phone)
    contact.save()
    message('Phone added successfully')


def add_email(contact_id, email):
    contact = Contact.__objects.get(id=ObjectId(contact_id))
    contact_email = contact.email
    if contact_email == email:
        warning('This email already exists!')
    else:
        contact.email = email
        contact.save()
        message('Email added successfully')


def add_contact(first_name, last_name, phone, email):
    newContact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone
    )
    newContact.save()


@LruCache
def get_contact_by_id(contact_id):
    try:
        contact = Contact.__objects.get(id=ObjectId(contact_id))
        contact_cache ={
        'first_name': contact.first_name,
        'last_name': contact.last_name,
        'phone': contact.phone,
        'email': contact.email
        }
        return contact_cache
    except DoesNotExist:
        warning('Contact does not exists!')


def delete_contact(contact_id):
    contact = Contact.__objects.get(id=ObjectId(contact_id))
    contact.delete()
    message('Contact deleted successfully')
