from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from django.urls import reverse_lazy

from workers_tree.employees.models import Employee
from workers_tree.employees.filter import EmployeeFilter
from workers_tree.employees.filter import EmployeeFilterFormHelper
from workers_tree.employees.tables import EmployeeTable


CHANGE_EMPLOYEE_DENIED_MESSAGE = "You can't change employee from another division"
NOT_LOGGED_IN_MESSAGE = "You need to log in"


class FilterEmployeesMixin:

    def get_queryset(self, **kwargs):
        return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = EmployeeFilter(
            self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = EmployeeFilterFormHelper()
        table = EmployeeTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


class PersonalCabinetMixin:

    def get_queryset(self, **kwargs):
        return Employee.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_queryset(**kwargs)
        user = get_user_model().objects.get(employee=employee)
        image_url = user.image.url
        employees = Employee.objects.filter(manager=employee)
        context['employee'] = employee
        context['user'] = user
        context['image_url'] = image_url
        context['employees'] = employees
        return context


class PersonnelManagementMixin:

    def get_queryset(self, **kwargs):
        return Employee.objects.filter(
            manager=self.request.user.employee).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = self.get_queryset(**kwargs)
        context['employees'] = employees
        return context


class ManagerPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        if (self.kwargs['pk'],) not in list(Employee.objects.filter(
                manager=self.request.user.employee).values_list('id')):
            messages.error(self.request, CHANGE_EMPLOYEE_DENIED_MESSAGE)
            return False
        return True

    def handle_no_permission(request):
        return redirect(reverse_lazy('cabinet'))


class EmployeeUpdateMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = Employee.objects.get(id=self.kwargs['pk'])
        user = get_user_model().objects.get(employee=employee)
        # image_url = user.image.url
        context['employee'] = employee
        context['user'] = user
        # context['image_url'] = image_url
        return context
