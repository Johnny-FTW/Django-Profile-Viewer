from django.contrib import admin

# Register your models here.
from viewer.models import Gender, Profile, Photo, Status, Comment

admin.site.register(Gender)
admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(Status)
admin.site.register(Comment)