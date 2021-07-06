from django.test import TestCase
from accounts.models import CustomUserManager

# Create your tests here


class TestCustomUserManager(TestCase):

    def setUp(self):
        self.user = CustomUserManager()

    def test_custom_user_manager(self):
        new_user = self.user
        self.assertIsInstance(new_user, CustomUserManager)

    





