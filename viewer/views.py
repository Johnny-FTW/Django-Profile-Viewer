from django.contrib.auth.forms import UserCreationForm
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




class SignUpView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        self.make_profile()
        return response

    def make_profile(self):
        Profile.objects.create(user=self.object)


