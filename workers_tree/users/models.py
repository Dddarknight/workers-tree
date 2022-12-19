from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class EmployeeUser(AbstractUser):
    username = models.TextField(unique=True)
    image = models.ImageField(
        upload_to='images', blank=True, default='images/test_picture.jpeg')

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        url = reverse_lazy('employees')
        return f'{url}{self.id}'
