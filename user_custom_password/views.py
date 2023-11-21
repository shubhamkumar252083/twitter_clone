from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from user.forms import CustomPasswordChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        super().form_valid(form)
        # Update the session to keep the user logged in
        update_session_auth_hash(self.request, self.request.user)
