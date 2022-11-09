from django.contrib.auth import get_user_model
from django.test import TestCase

from workers_tree.employees.models import Employee
from workers_tree.utils import get_test_data


class TestContainer(TestCase):
    test_data_users = get_test_data('users.json')
    test_data_employees = get_test_data('employees.json')

    def create_user(self, user):
        return get_user_model().objects.create(
            first_name=self.test_data_users['users'][user]['first_name'],
            last_name=self.test_data_users['users'][user]['last_name'],
            username=self.test_data_users['users'][user]['username'],
            password=self.test_data_users['users'][user]['password'])

    def create_employee(self, user, manager, employee):
        job_title = (
            self.test_data_employees['employees'][employee]['job_title']
        )
        employment_date = (
            self.test_data_employees['employees'][employee]['employment_date']
        )
        salary = (
            self.test_data_employees['employees'][employee]['salary']
        )
        if manager:
            return Employee.objects.create(
                user=user,
                job_title=job_title,
                employment_date=employment_date,
                salary=salary,
                manager=manager)
        return Employee.objects.create(
                user=user,
                job_title=job_title,
                employment_date=employment_date,
                salary=salary)
