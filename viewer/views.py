from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from viewer.forms import SignUpForm
from viewer.models import Profile

@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request,'profile.html',context)


def edit_profile(request):
    return render(request, 'edit_profile.html')


def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {'profile': profile, 'user':user}
    return render(request, 'profile.html', context)


def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

def search(request):
    usernames = None
    real_usernames = None
    if request.method == 'POST':
        search = request.POST.get('query')
        search = search.strip()
        if len(search) > 0:
            usernames = User.objects.filter(username__contains=search)
            real_usernames = User.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))

    context = {'search': search, 'usernames': usernames, 'real_usernames': real_usernames}
    return render(request, 'search.html', context)



def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
        return render(request=request, template_name="signup.html", context={"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
