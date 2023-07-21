"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    """Test Models."""

    def test_with_email(self):
        "Test creating a user with an email is succeessfull"
        email = 'test1234@gmail.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))