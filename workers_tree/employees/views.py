from django.views import generic
from django_tables2 import RequestConfig
from workers_tree.employees.models import Employee
from workers_tree.employees.tables import EmployeeTable
from workers_tree.employees.filter import EmployeeFilter
from workers_tree.employees.filter import EmployeeFilterFormHelper
from workers_tree.employees.utils import build_tree


class IndexView(generic.TemplateView):
    template_name = 'index.html'
    extra_context = {'tree': build_tree()}


class EmployeesView(generic.TemplateView):
    template_name = "filter_sort_form.html"

    def get_queryset(self, **kwargs):
        return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeesView, self).get_context_data(**kwargs)
        filter = EmployeeFilter(
            self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = EmployeeFilterFormHelper()
        table = EmployeeTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context
