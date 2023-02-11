from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from viewer.forms import SignUpForm
from viewer.models import Profile


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request,'profile.html',context)


def home(request):
    return render(request,'home.html')


def register_request(request):
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



# def logout_view(request):
#     logout(request)
#     return redirect('home')





# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 # Return an 'invalid login' error message.
#                 ...
#         else:
#             # The form is not valid
#             ...
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
