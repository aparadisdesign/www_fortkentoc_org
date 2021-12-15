from django.db.utils import IntegrityError
from django.test import TestCase
from .models import MembershipType


class MembershipTestCase(TestCase):
    def setUp(self):
        MembershipType.objects.create(name="Adult", year="2022", price=60)

    def test_membership_year_and_name_unique_together(self):
        with self.assertRaises(IntegrityError):
            membership = MembershipType.objects.create(name="Adult", year="2022", price=60)
            membership.save()
