from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from workers_tree.users.forms import SignUpForm, LoginForm
from workers_tree.users.mixins import UserPermissionsMixin
from workers_tree.users.mixins import UserFormLoginMixin
from workers_tree.users.mixins import MessageLogOutMixin


REGISTRATION_SUCCESS_MESSAGE = 'User was registered'
UPDATE_USER_SUCCESS_MESSAGE = 'User was updated successfully'
DELETE_SUCCESS_MESSAGE = 'User was deleted successfully'
LOGGED_IN_MESSAGE = 'You are logged in.'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = REGISTRATION_SUCCESS_MESSAGE

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class UserUpdateView(UserPermissionsMixin,
                     SuccessMessageMixin,
                     UserFormLoginMixin,
                     UpdateView):
    model = get_user_model()
    template_name = 'users/update.html'
    form_class = SignUpForm
    success_url = reverse_lazy('/')
    success_message = UPDATE_USER_SUCCESS_MESSAGE
    login_url = reverse_lazy('login')
    redirect_field_name = None


class UserDeleteView(UserPermissionsMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('/')
    success_message = DELETE_SUCCESS_MESSAGE


class LoginView_(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_message = LOGGED_IN_MESSAGE


class LogoutView_(MessageLogOutMixin, LogoutView):
    pass
