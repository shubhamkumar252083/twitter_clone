from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import *



def user(request):
    return HttpResponse("<h1>user</h1>")

urlpatterns = [
    path('', user, name="user"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('UserTweets/', UserTweets.as_view(), name="UserTweets"),
    path('MyDetail/', MyDetail.as_view(), name="MyDetail"),
    path('HashTags/', HashTags.as_view(), name="HashTags"),
    path('UserEditTweet/<int:tweet_id>/', UserEditTweet.as_view(), name='UserEditTweet'),

]
