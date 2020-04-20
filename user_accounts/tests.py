from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import login_signup

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('login_signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/login_signup/')
        self.assertEquals(view.func, login_signup)
