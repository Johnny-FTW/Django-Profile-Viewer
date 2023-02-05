from django.db import models

# Create your models here.
from django.db.models import *


class Gender(Model):
    name = CharField(max_length=50)


class Profile(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING)
    city = CharField(max_length=50)
    about = TextField(max_length=1024)