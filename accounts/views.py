from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')  # kam nás to přesměruje v případě úspěchu
    template_name = 'signup.html'  # použije se tento template