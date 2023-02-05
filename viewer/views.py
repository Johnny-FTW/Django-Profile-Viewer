from django.shortcuts import render

# Create your views here.
from viewer.models import Profile


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request,'profile.html',context)