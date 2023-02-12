from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import *


class Gender(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

class Photo(Model):
    link = CharField(max_length=1024, null=True)

class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING, null=True)
    city = CharField(max_length=50, null=True)
    about = TextField(max_length=1024, null=True)
    profile_picture = CharField(max_length=1024, null=True)
    photos = ForeignKey(Photo, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.user}'

# class UserFollowing(models.Model):
#     user_id = models.ForeignKey("User", related_name="following")
#
#     following_user_id = models.ForeignKey("User", related_name="followers")
#
#     # You can even add info about when user started following
#     created = models.DateTimeField(auto_now_add=True)