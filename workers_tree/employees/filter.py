import django_filters
from workers_tree.users.models import EmployeeUser
from workers_tree.employees.models import Employee

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class EmployeeFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        'name',
        'job_title',
        'employment_date',
        'salary',
        'manager',
        Submit('submit', 'Apply Filter'),
    )


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(
        field_name='user',
        queryset=EmployeeUser.objects.filter(employee__isnull=False))
    job_title = django_filters.AllValuesFilter()
    employment_date = django_filters.AllValuesFilter()
    salary = django_filters.AllValuesFilter()
    manager = django_filters.ModelChoiceFilter(
        field_name='manager',
        queryset=Employee.objects.all())
    image = EmployeeUser.objects.values('image')

    class Meta:
        model = Employee
        fields = ['name',
                  'job_title',
                  'employment_date',
                  'salary',
                  'manager']
