from django.urls import path

from viewer.views import *

urlpatterns = [

    path('my_profile/', my_profile, name='my_profile'),
    path('my_profile/edit_profile/', edit_profile_page, name='edit_profile_page'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name ='profile'),
    path('profile/followers/<str:username>/', followers_page, name='followers_page'),
    path('profile/following/<str:username>/', following_page, name='following_page'),

    path('news/',news, name='news'),
    path('news/like/', like, name='like'),
    path('news/dislike/', dislike, name='dislike'),

    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('', login_view, name='login_view'),

    path('search/', search, name='search'),
    path('follow/', follow, name='follow'),


    path('add_comment', add_comment, name='add_comment'),
    path('edit_comment/<pk>', edit_comment, name='edit_comment'),
    path('delete_comment/<pk>/', delete_comment, name='delete_comment'),

    path('post_status', post_status, name='post_status'),

]