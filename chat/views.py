from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    context={'users': users}
    return render(request, 'index.html', context)