from django.contrib import admin

# Register your models here.
from viewer.models import Gender, Profile

admin.site.register(Gender)
admin.site.register(Profile)
