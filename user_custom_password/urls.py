from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm  # Import your custom form

from django.urls import path

from .views import CustomPasswordChangeView  # Import your custom view
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    # Your other URL patterns here
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
