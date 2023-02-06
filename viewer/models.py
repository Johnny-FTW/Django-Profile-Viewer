from django.db import models

# Create your models here.
from django.db.models import *


class Gender(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING)
    city = CharField(max_length=50)
    about = TextField(max_length=1024)
    profile_picture = CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'