from django.urls import path

from chat.views import *

urlpatterns = [
    path('chat/', index, name='index'),
    path('chat/<str:username>/', chat, name='chat'),
    path('sent_msg/<str:username>/', sent_messages, name='sent_messages'),
    path('rec_msg/<str:username>/', received_messages, name='received_messages'),
    path('notification', chat_notification, name='notification'),

]