from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


LOG_IN_ERROR_MESSAGE = 'Please enter a valid username and password.'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First name',
                                 label_suffix='',
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First name',
                                            'class': 'form-control', }))
    last_name = forms.CharField(label='Last name',
                                label_suffix='',
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last name',
                                           'class': 'form-control', }))
    username = forms.CharField(label='Username',
                               max_length=150,
                               label_suffix='',
                               required=True,
                               help_text='Required field',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username',
                                          'autofocus': True,
                                          'class': 'form-control', }),
                               error_messages={'unique': 'User already exists'})
    password1 = forms.CharField(label='Password',
                                label_suffix='',
                                required=True,
                                help_text="Your password doesn't "
                                          "meet security requirements",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Password',
                                           'class': 'form-control', }))
    password2 = forms.CharField(label='Confirm password',
                                label_suffix='',
                                required=True,
                                help_text='Please enter a password again',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Confirm password',
                                        'class': 'form-control', }))
    image = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2', 'image')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               label_suffix='',
                               max_length=150,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username',
                                          'class': 'form-control',
                                          'autofocus': True,
                                          'style': 'max-width: 24em', }))
    password = forms.CharField(label='Password',
                               label_suffix='',
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'style': 'max-width: 24em', }))
    error_messages = {'invalid_login': LOG_IN_ERROR_MESSAGE}

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
