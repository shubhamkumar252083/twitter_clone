from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>home</h1>")

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('hash_url/', include('hash_url.urls')),
]
