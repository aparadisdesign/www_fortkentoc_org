import uuid as uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from website.models import User

MEMBERSHIP_TYPE_CHOICES = (
    ("Adult", "Adult"),
    ("Family", "Family"),
    ("Student", "Student"),
)

PAYMENT_TYPE_CHOICES = (
    ("Cash", "Cash"),
    ("Check", "Check"),
    ("Paypal", "Paypal"),
    ("Gratis", "Gratis"),
    ("Gift Cert", "Gift Cert")
)


class MembershipType(models.Model):
    name = models.CharField(
        max_length=10,
        choices=MEMBERSHIP_TYPE_CHOICES,
        verbose_name="Member Type Name",
        help_text="Please select the type of membership",
        blank=False,
        null=False,
    )
    year = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Membership Year"
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ["name", "year"]

    def __str__(self):
        return f"{self.name} - {self.year}"


class Membership(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(to=MembershipType, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(max_digits=5, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    payment_date = models.DateField()
    notes = models.TextField(null=True, blank=True)


class Member(models.Model):
    membership = models.ForeignKey(to=Membership, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=24, null=False, blank=False)
    first_name = models.CharField(max_length=24, null=False, blank=False)
    address = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=24, null=True, blank=True)
    state = models.CharField(max_length=24, null=True, blank=True)
    postal_code = models.CharField(max_length=14, null=True, blank=True)