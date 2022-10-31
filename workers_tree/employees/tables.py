import django_tables2 as tables
from workers_tree.employees.models import Employee


class EmployeeTable(tables.Table):

    class Meta:
        model = Employee
        fields = ('name',
                  'job_title',
                  'employment_date',
                  'salary',
                  'manager',
                  'image')
