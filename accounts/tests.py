from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountsTests(TestCase):

    def test_login_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='example@lakesite.net', password='example')

        self.assertEqual(user.email, 'example@lakesite.net')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="example")
        with self.assertRaises(ValidationError):
            User.objects.create_user(email='invalid', password="example")
