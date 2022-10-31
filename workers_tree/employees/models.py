from django.db import models
from django.contrib.auth import get_user_model


class Employee(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        null=False,
        on_delete=models.CASCADE,
        related_query_name="employee")
    job_title = models.TextField(max_length=20, null=False)
    employment_date = models.DateTimeField(null=False)
    salary = models.IntegerField()
    manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.get_full_name()

    def name(self):
        return self.user.get_full_name()
