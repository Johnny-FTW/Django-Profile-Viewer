import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from chat.forms import ChatMessageForm
from chat.models import ChatMessage


# Create your views here.


@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    context={'users': users}
    return render(request, 'index.html', context)


@login_required
def chat(request, username):
    friend = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = request.user
            chat_message.msg_receiver = friend
            chat_message.save()
            return redirect('chat', username=username)
    context={'friend': friend, 'users':users, 'form':form, 'chats':chats }
    return render(request, 'chat.html', context)


def sent_messages(request, pk):
    friend = User.objects.get(id=pk)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=request.user, msg_receiver=friend, seen=False)
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)