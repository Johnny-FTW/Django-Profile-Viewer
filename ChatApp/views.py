from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

#User = get_user_model()


def chat_page(request):
    users = User.objects.exclude(username=request.user.username)
    context = {'users':users}
    return render(request, 'main_chat.html', context)