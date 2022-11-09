from django.test import TestCase

from workers_tree.employees.forms import EmployeeUpdateForm
from workers_tree.test_container import TestContainer
from workers_tree.utils import get_test_data


test_container = TestContainer()


class UserValidFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = test_container.create_user('user1')
        cls.user2 = test_container.create_user('user2')
        cls.user3 = test_container.create_user('user3')
        cls.manager1 = test_container.create_employee(
            cls.user1, None, 'employee1')
        cls.manager2 = test_container.create_employee(
            cls.user2, None, 'employee2')
        cls.employee = test_container.create_employee(
            cls.user3, cls.manager1, 'employee3')
        cls.employee_new_data = get_test_data(
            'employees.json')['employees']['employee4']

    def test_valid_form(self):
        data = {'job_title': self.employee_new_data['job_title'],
                'salary': self.employee_new_data['salary'],
                'manager': self.manager2}
        form = EmployeeUpdateForm(data=data)
        self.assertTrue(form.is_valid())
