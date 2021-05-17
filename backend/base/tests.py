from django.test import TestCase
from base.models import *

# Create your tests here.
class StaffTestCase(TestCase):
    def setUp(self):
        # Create Users.
        u1 = User.objects.create(username='u@email.com', password='admin')

        # Create Staff.
        Staff.objects.create(email='u@email.com', staffType='admin')

    def test_email(self):
        staff = Staff.objects.get(email='u@email.com')
        self.assertNotEqual(staff.email, '')

    def test_email_valid(self):
        staff = Staff.objects.get(email='u@email.com')
        self.assertTrue(User.objects.get(username=staff.email))
