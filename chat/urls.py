from django.urls import path

from chat.views import *

urlpatterns = [
    path('chat/', index, name='index'),
    path('chat/<str:username>/', chat, name='chat'),
    path('sent_msg/<str:pk>/', sent_messages, name='sent_msg'),
]