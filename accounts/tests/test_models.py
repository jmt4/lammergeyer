from django.test import TestCase
from django.core.exceptions import ValidationError

from accounts.models import CustomUser

class UserModelTests(TestCase):

	def test_default_values(self):
		user = CustomUser()
		self.assertEqual(user.email, '')
		self.assertEqual(user.password, '')
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_string_representation(self):
		user = CustomUser(email='jj@gmail.com', password='1234')
		self.assertEqual(str(user), 'jj@gmail.com')
		self.assertEqual(user.password, '1234')

class UserManagerTests(TestCase):

	def test_user_manager_creates_user(self):
		user = CustomUser.objects.create_user(email='jj@gmail.com', password='1234')
		self.assertEqual(CustomUser.objects.count(), 1)

	def test_user_manager_create_user_values_and_default_values(self):
		CustomUser.objects.create_user(email='jj@gmail.com', password='1234')
		first_user = CustomUser.objects.first()
		self.assertEqual(first_user.email, 'jj@gmail.com')
		self.assertEqual(first_user.password, '1234')
		self.assertFalse(first_user.is_staff)
		self.assertFalse(first_user.is_superuser)

	def test_user_manager_forbids_empty_email(self):
		with self.assertRaises(ValueError):
			CustomUser.objects.create_user(email='', password='1234')