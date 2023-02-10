

from django.contrib.auth.models import User


from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from viewer.forms import SignUpForm
from viewer.models import Profile


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request,'profile.html',context)


def home(request):
    return render(request,'home.html')


# def sign_up(request):
#     return render(request,'signup.html')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    #profile = Profile.objects.create(user=)
