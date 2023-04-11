from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ChatApp.forms import ChatMessageForm

# Create your views here.


@login_required
def index(request):
    # users = User.objects.exclude(username=request.user.username)
    users = User.objects.all()
    context={'users': users}
    return render(request, 'index.html', context)


@login_required
def chat_page(request, pk):
    user_receiver = User.objects.get(id=pk)

    users = User.objects.exclude(username=request.user.username)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = request.user
            chat_message.msg_receiver = user_receiver
            chat_message.save()
            return redirect('chat_page', pk=user_receiver.id)
    context = {'users':users, 'user_receiver':user_receiver, "form":form}
    return render(request, 'main_chat.html', context)