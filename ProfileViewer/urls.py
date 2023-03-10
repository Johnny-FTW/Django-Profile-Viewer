"""ProfileViewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import my_profile, home, signup_view, logout_view, login_view, profile, search, edit_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_profile/', my_profile, name='my_profile'),
    path('my_profile/edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name ='profile'),
    path('',home, name='home'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    path('search/', search, name='search'),
]
