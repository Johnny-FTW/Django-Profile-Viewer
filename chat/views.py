import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from chat.forms import ChatMessageForm
from chat.models import ChatMessage


# Create your views here.

@login_required
def sent_messages(request, username):
    friend = User.objects.get(username=username)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=request.user, msg_receiver=friend,
                                                  seen=False)
    print(new_chat)
    return JsonResponse({'body': new_chat_message.body}, safe=False)


@login_required
def received_messages(request, username):
    friend = User.objects.get(username=username)
    arr = []
    chats = ChatMessage.objects.filter(msg_sender=friend, msg_receiver=request.user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)


@login_required
def chat_notification(request):
    users = User.objects.filter(profile__followers=request.user, id__in=request.user.profile.followers.all())
    arr = []
    for user in users:
        chats = ChatMessage.objects.filter(msg_sender__id=user.id, msg_receiver=request.user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)


@login_required
def chat(request, username):
    friend = get_object_or_404(User, username=username)
    profile = request.user.profile

    if friend not in profile.followers.all():
        return HttpResponseForbidden("You can only chat with your friends.")

    friend_profile = friend.profile
    if request.user not in friend_profile.followers.all():
        return HttpResponseForbidden("You can only chat with your friends.")

    users = User.objects.filter(profile__followers=request.user, id__in=request.user.profile.followers.all())
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=friend, msg_receiver=request.user, seen=False)
    rec_chats.update(seen=True)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = request.user
            chat_message.msg_receiver = friend
            chat_message.save()
            return redirect('chat', username=username)
    context = {'friend': friend, 'users': users, 'form': form, 'chats': chats, 'num': rec_chats.count()}
    return render(request, 'chat.html', context)


@login_required
def index(request):
    users = User.objects.filter(profile__followers=request.user, id__in=request.user.profile.followers.all())
    context = {'users':users}
    return render(request, 'index.html', context)