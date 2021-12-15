import uuid as uuid
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

MEMBERSHIP_TYPE_CHOICES = (
    ("Adult", "Adult"),
    ("Family", "Family"),
    ("Student", "Student"),
)

PAYMENT_TYPE_CHOICES = (
    ("Cash", "Cash"),
    ("Check", "Check"),
    ("Paypal", "Paypal")
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class MembershipType(models.Model):
    name = models.CharField(
        max_length=7,
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
    payment_type = models.CharField(max_length=6, choices=PAYMENT_TYPE_CHOICES)
    payment_date = models.DateField()


class Member(models.Model):
    membership = models.ForeignKey(to=Membership, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=24, null=False, blank=False)
    first_name = models.CharField(max_length=24, null=False, blank=False)
    address = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=24, null=True, blank=True)
    state = models.CharField(max_length=24, null=True, blank=True)
    postal_code = models.CharField(max_length=14, null=True, blank=True)