from django import forms
from workers_tree.employees.models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    job_title = forms.CharField(label='Job Title',
                                label_suffix='',
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Job Title',
                                           'class': 'form-control', }))
    salary = forms.IntegerField(label='Salary',
                                label_suffix='',
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Salary',
                                           'class': 'form-control', }))
    manager = forms.ModelChoiceField(
        label='Manager',
        label_suffix='',
        required=True,
        widget=forms.Select(
            attrs={'style': 'min-height: 50px;', }),
        queryset=Employee.objects.all())


    class Meta:
        model = Employee
        fields = (
            'job_title',
            'salary',
            'manager'
            )
