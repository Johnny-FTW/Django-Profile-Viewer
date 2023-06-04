from urllib.error import URLError
from urllib.request import urlopen
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from viewer.forms import SignUpForm
from viewer.models import Profile, Gender, Photo, Status, Comment


@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    photos = Photo.objects.filter(profile=profile)
    context = {'profile': profile, 'photos': photos}
    return render(request,'profile.html',context)


@login_required
def edit_profile_page(request):
    profile = Profile.objects.get(user=request.user)
    genders = Gender.objects.all()
    photos = profile.photos.all()
    context = {'profile': profile, 'genders':genders, 'photos': photos}
    return render(request, 'edit_profile.html', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    user = request.user
    genders = Gender.objects.all()

    if request.method == 'POST':

        photos = request.POST.getlist('photos[]')

        profile_picture = request.POST.get('photo').strip()
        city = request.POST.get('city').strip()
        about = request.POST.get('about').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        gender = request.POST.get('gender', '')
        cover_picture = request.POST.get('cover').strip()

        if profile_picture:
            url_validator = URLValidator()
            try:
                url_validator(profile_picture)
                with urlopen(profile_picture):
                    profile.profile_picture = profile_picture
            except (ValidationError, URLError):
                pass
        else:
            profile.profile_picture = None

        profile.city = city
        profile.about = about
        profile.cover_picture = cover_picture

        if gender:
            selected_gender = Gender.objects.get(id=gender)
            profile.gender = selected_gender
        else:
            profile.gender = None

        with transaction.atomic():
            profile.photos.all().delete()
            for photo_link in photos:
                if photo_link:
                    photo = Photo(link=photo_link)
                    photo.save()
                    profile.photos.add(photo)

        profile.save()

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('my_profile/edit_profile/')

    photos = profile.photos.all()
    return render(request, 'edit_profile.html', context={'profile': profile, 'genders': genders, 'photos': photos})


@login_required
def followers_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    followers = profile.followers.all()
    context = {'followers': followers, 'username':username}
    return render(request, 'followers.html', context)


@login_required
def following_page(request, username):
    user = User.objects.get(username=username)
    following = user.following.all()
    context = {'following': following, 'username': username}
    return render(request, 'following.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    photos = Photo.objects.filter(profile=profile)
    context = {'profile': profile, 'user':user, 'photos':photos}
    return render(request, 'profile.html', context)


@login_required
def news(request):
    users = User.objects.filter(profile__followers=request.user, id__in=request.user.profile.followers.all())
    statuses = Status.objects.filter(Q(user__in=users) | Q(user=request.user))
    comments = Comment.objects.all()
    context = {'statuses': statuses, 'comments':comments}
    return render(request, 'news.html', context)


def search(request):
    usernames = None
    real_usernames = None
    if request.method == 'POST':
        search = request.POST.get('query')
        search = search.strip()
        if len(search) > 0:
            usernames = User.objects.filter(username__contains=search)
            real_usernames = User.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        if not usernames and not real_usernames:
            messages.error(request, "No match.")
    context = {'usernames': usernames, 'real_usernames': real_usernames}
    return render(request, 'search.html', context)


@login_required
def post_status(request):
    if request.method == 'POST':
        status = request.POST.get('status').strip()
        if len(status) > 0:
            Status.objects.create(
                user = request.user,
                text = status,
            )
            messages.success(request, "Your status was posted.")
        else:
            messages.error(request, "Cant post your status.")
    return redirect('/news/')


@login_required
def follow(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_id')
        profile = Profile.objects.get(id=pk)
        if not request.user in profile.followers.all():
            profile.followers.add(request.user)
            messages.success(request, "You are following this profile!")
        else:
            profile.followers.remove(request.user)
            messages.warning(request, "You unfollowed this profile!")

        redirect_url = request.GET.get('redirect_url')
        if redirect_url:
            return redirect(redirect_url)
        else:
            return redirect(f'/profile/{profile.user.username}/')



@login_required
def like(request):
    if request.method == 'POST':
        pk = request.POST.get('status_id')
        status = Status.objects.get(id=pk)
        if not request.user in status.likes.all():
            status.likes.add(request.user)
            if request.user in status.dislikes.all():
                status.dislikes.remove(request.user)
        else:
            status.likes.remove(request.user)
        like_count = status.likes.count()
        return JsonResponse({'like_count': like_count})
    else:
        return HttpResponse('Invalid request method')


@login_required
def dislike(request):
    if request.method == 'POST':
        pk = request.POST.get('status_id')
        status = Status.objects.get(id=pk)
        if not request.user in status.dislikes.all():
            status.dislikes.add(request.user)
            if request.user in status.likes.all():
                status.likes.remove(request.user)
        else:
            status.dislikes.remove(request.user)
        dislike_count = status.dislikes.count()
        return JsonResponse({'dislike_count': dislike_count})
    else:
        return HttpResponse('Invalid request method')


@login_required
def add_comment(request):
    if request.method == 'POST':
        pk = request.POST.get('status_id')
        comment = request.POST.get('comment').strip()
        if len(comment) > 0:
            Comment.objects.create(
                status = Status.objects.get(id=pk),
                user = request.user,
                text = comment
            )
            messages.success(request, "Your comment was posted.")
        else:
            messages.error(request, "Cant post your comment.")
    return redirect('/news/')


@login_required
def edit_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment_text = request.POST.get('comment').strip()
            comment.text = comment_text
            comment.save()
            messages.warning(request, "Your comment was edited.")
            return redirect('/news/')
        context = {'comment': comment}
        return render(request, 'news.html', context)
    return redirect('news.html')


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            messages.warning(request, "Your comment was deleted.")
            return redirect("/news/")
        context = {'comment': comment}
        return render(request, 'news.html', context)
    return redirect("/news/")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('news')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
    return render(request=request, template_name="signup.html", context={"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.warning(request, "You have been successfully logged out.")
    return redirect('login_view')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('news')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('news')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
