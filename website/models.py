from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.translation import gettext as _


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


class BoardMember(models.Model):
    first_name = models.CharField(max_length=65, null=False, blank=False)
    last_name = models.CharField(max_length=65, null=False, blank=False)
    office_held = models.CharField(max_length=99, null=True, blank=True)
    image = models.ImageField(
        upload_to="uploads/board_members/% Y/% m/% d/", null=True, blank=True
    )

    def __str__(self):
        if self.office_held:
            return f"{self.last_name}, {self.first_name} - {self.office_held}"
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Board Member"
        verbose_name_plural = "Board Members"


class Sponsor(models.Model):
    name = models.CharField(max_length=65, null=False, blank=False)
    level = models.CharField(max_length=15, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to="uploads/sponsors/% Y/% m/% d/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["start_date", "name"]
        verbose_name = ("Sponsor",)
        verbose_name_plural = "Sponsors"


class Coach(models.Model):
    last_name = models.CharField(max_length=45, null=False, blank=False)
    first_name = models.CharField(max_length=45, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    biography = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"


class Activity(models.Model):
    season = models.CharField(max_length=6, choices=(("Winter", "Winter"), ("Summer", "Summer")), default="Winter", null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ["name"]