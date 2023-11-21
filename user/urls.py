from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import UserLoginView, UserTweets, CustomLogoutView, MyDetail



def user(request):
    return HttpResponse("<h1>user</h1>")

urlpatterns = [
    path('', user, name="user"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('UserTweets/', UserTweets.as_view(), name="UserTweets"),
    path('MyDetail/', MyDetail.as_view(), name="MyDetail"),

]
