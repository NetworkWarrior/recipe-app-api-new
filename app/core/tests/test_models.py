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

    def test_new_user_email_normilized(self):
        """Test if email is normilized for a new user."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
