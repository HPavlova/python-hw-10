from mongoengine import *


class Contact(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True)
    phone = ListField(StringField())

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
