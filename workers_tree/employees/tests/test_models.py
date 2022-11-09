from django.test import TestCase

from workers_tree.employees.models import Employee
from workers_tree.test_container import TestContainer
from workers_tree.utils import get_test_data


test_container = TestContainer()


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = test_container.create_user('user1')
        cls.user2 = test_container.create_user('user2')
        cls.manager = test_container.create_employee(
            cls.user1, None, 'employee1')
        cls.employee = test_container.create_employee(
            cls.user2, cls.manager, 'employee2')
        cls.manager_data = get_test_data(
            'employees.json')['employees']['employee1']
        cls.employee_data = get_test_data(
            'employees.json')['employees']['employee2']

    def test_task_creation(self):
        self.assertTrue(isinstance(self.manager, Employee))
        self.assertTrue(isinstance(self.employee, Employee))
        self.assertEqual(
            self.manager.job_title, self.manager_data['job_title'])
        self.assertEqual(
            self.manager.employment_date, self.manager_data['employment_date'])
        self.assertEqual(
            self.manager.salary, self.manager_data['salary'])
        self.assertEqual(
            self.manager.user, self.user1)
        self.assertEqual(
            self.employee.job_title, self.employee_data['job_title'])
        self.assertEqual(
            self.employee.employment_date,
            self.employee_data['employment_date'])
        self.assertEqual(
            self.employee.salary, self.employee_data['salary'])
        self.assertEqual(
            self.employee.user, self.user2)
        self.assertEqual(
            self.employee.manager, self.manager)
