
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', HashUrl.as_view(), name="HashUrl"),
    path('encode/<str:encoded_id>/', CheckHash.as_view(), name='CheckHash'),
]
