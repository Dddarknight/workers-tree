from django.test import TestCase
from django.test import Client

from workers_tree.employees.models import Employee
from workers_tree.test_container import TestContainer


test_container = TestContainer()


class TreeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = test_container.create_user('user1')
        cls.user2 = test_container.create_user('user2')
        cls.user3 = test_container.create_user('user3')
        cls.user4 = test_container.create_user('user4')
        cls.user5 = test_container.create_user('user5')
        cls.employee1 = test_container.create_employee(
            cls.user1, None, 'employee1')
        cls.employee2 = test_container.create_employee(
            cls.user2, cls.employee1, 'employee2')
        cls.employee3 = test_container.create_employee(
            cls.user3, cls.employee2, 'employee3')
        cls.employee4 = test_container.create_employee(
            cls.user4, cls.employee2, 'employee4')
        cls.employee5 = test_container.create_employee(
            cls.user5, cls.employee3, 'employee5')

    def test_tree(self):
        c = Client()
        x = Employee.objects.filter(manager__isnull=True)
        print(x)
        response = c.get('/')
        print(response.context)
        employees = Employee.objects.all()
        for employee in employees:
            self.assertContains(response, employee.name())
