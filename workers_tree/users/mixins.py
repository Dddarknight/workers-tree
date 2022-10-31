from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate


CHANGE_USER_DENIED_MESSAGE = 'You have no rights to change another user'
NOT_LOGGED_IN_MESSAGE = 'You are not authorized. Please, log in.'
LOGGED_OUT_MESSAGE = 'You are logged out'


class UserPassesTestMixin_(UserPassesTestMixin):

    def test_func(self):
        if self.kwargs['pk'] != self.request.user.id:
            messages.error(self.request, CHANGE_USER_DENIED_MESSAGE)
            return False
        return True

    def handle_no_permission(request):
        return redirect(reverse_lazy('users'))


class UserPermissionsMixin(LoginRequiredMixin, UserPassesTestMixin_):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, NOT_LOGGED_IN_MESSAGE)
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class UserFormLoginMixin:

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


class MessageLogOutMixin:

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, LOGGED_OUT_MESSAGE)
        return response
