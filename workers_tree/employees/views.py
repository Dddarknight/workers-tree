from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from workers_tree.employees.models import Employee
from workers_tree.employees.mixins import FilterEmployeesMixin
from workers_tree.employees.mixins import PersonalCabinetMixin
from workers_tree.employees.mixins import PersonnelManagementMixin
from workers_tree.employees.mixins import EmployeeUpdateMixin
from workers_tree.employees.mixins import ManagerPassesTestMixin
from workers_tree.employees.forms import EmployeeUpdateForm
from workers_tree.employees.utils import build_tree, build_js_tree
from django.http import JsonResponse

from django.http import HttpResponse
from django.template import loader


EMPLOYEE_UPDATE_SUCCESS_MESSAGE = "Employee was updated successfully"


def index(request):
    template = loader.get_template('index.html')
    heads = Employee.objects.filter(manager__isnull=True)
    tree = build_tree(heads)
    context = {'tree': tree}
    return HttpResponse(template.render(context, request))


class TreeView(generic.TemplateView):
    template_name = 'employees/js-tree.html'


class TreeJsonView(generic.View):

    def get(self, *args, **kwargs):
        return JsonResponse(build_js_tree(), safe=False)


class EmployeesView(FilterEmployeesMixin, generic.TemplateView):
    template_name = "employees/filter_sort_form.html"


class PersonalCabinet(PersonalCabinetMixin, generic.TemplateView):
    template_name = "employees/cabinet.html"


class PersonnelManagement(PersonnelManagementMixin, generic.TemplateView):
    template_name = "employees/management.html"


class EmployeeUpdateView(EmployeeUpdateMixin,
                         ManagerPassesTestMixin,
                         SuccessMessageMixin,
                         UpdateView):
    model = Employee
    template_name = "employees/employee.html"
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('cabinet')
    success_message = EMPLOYEE_UPDATE_SUCCESS_MESSAGE
    login_url = reverse_lazy('login')
    redirect_field_name = None


class JsEmployeesView(generic.ListView):
    template_name = "employees/js_sort_filter.html"
    model = Employee
