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

    def __str__(self):
        return f'{self.link}'


class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    about = TextField(max_length=1024, null=True, blank=True)
    profile_picture = CharField(max_length=1024, null=True, blank=True)
    photos = ManyToManyField(Photo, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return f'{self.user}'


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_statuses')
    dislikes = models.ManyToManyField(User, related_name='disliked_statuses')

    class Meta:
        ordering = ['-date_created']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)