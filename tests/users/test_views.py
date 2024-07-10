from django.urls import reverse
from django.test import TestCase

from users.models import User


class UsersViewsTestTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='admin', password='admin')

    def test_login_view(self):
        response = self.client.get(reverse('login'))

        assert response.status_code == 200
        assert '<html' in response.content.decode()
        assert (
            """<input class="ml-12 rounded-md w-4/6 block text-slate-700" type="text" name="email" value="">"""
            in response.content.decode()
        )

    def test_login_view_authenticated(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('login'))

        assert response.status_code == 302
