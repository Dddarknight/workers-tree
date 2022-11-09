from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

from workers_tree.utils import get_test_data, get_picture
from django.core.files.uploadedfile import SimpleUploadedFile
from workers_tree.test_container import TestContainer


test_container = TestContainer()


class UserCreationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1_data = get_test_data('users.json')['users']['user1']
        cls.first_name = cls.user1_data['first_name']
        cls.last_name = cls.user1_data['last_name']
        cls.username = cls.user1_data['username']
        cls.password = cls.user1_data['password']
        cls.image = SimpleUploadedFile(
            name='test_picture.jpeg',
            content=get_picture('test_picture.jpeg'))

    def test_register_user(self):
        c = Client()
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'image': self.image
            }
        c.post('/users/sign-up/', data)
        user = get_user_model().objects.get(first_name='John')
        assert user.last_name == self.last_name
        assert user.username == self.username


class UserUpdateDeleteTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.user1_data = get_test_data('users.json')['users']['user1']
        cls.user2_data = get_test_data('users.json')['users']['user2']
        cls.first_name = cls.user1_data['first_name']
        cls.last_name = cls.user1_data['last_name']
        cls.username = cls.user2_data['username']
        cls.password = cls.user1_data['password']

    def test_update_user(self):
        c = Client()
        c.force_login(self.user)
        new_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'password1': self.password,
            'password2': self.password}
        c.post(f'/users/{self.user.id}/update/', new_data)
        user = get_user_model().objects.get(first_name=self.first_name)
        assert user.last_name == self.last_name
        assert user.username == self.username

    def test_delete_user(self):
        c = Client()
        c.force_login(self.user)
        c.post(f'/users/{self.user.id}/delete/')
        users = []
        for user in get_user_model().objects.all():
            users.append(user)
        assert not users


class UserViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')

    def test_create_view(self):
        c = Client()
        response = c.get(reverse_lazy('sign-up'))
        required_content_elements = [
            'First name', 'Last name', 'Username',
            'Password', 'Confirm password']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/sign-up.html')
        for element in required_content_elements:
            self.assertContains(response, element)

    def test_update_view(self):
        c = Client()
        c.force_login(self.user)
        response = c.get(reverse_lazy('update', args=[self.user.id]))
        required_content_elements = [
            'First name', 'Last name', 'Username',
            'Password', 'Confirm password']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        for element in required_content_elements:
            self.assertContains(response, element)

    def test_delete_view(self):
        c = Client()
        c.force_login(self.user)
        response = c.get(reverse_lazy('delete', args=[self.user.id]))
        required_content_elements = [
            'Delete user',
            'Are you sure you want to delete John Black ?']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')
        for element in required_content_elements:
            self.assertContains(response, element)
