from django.db import models


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


# Create your models here.
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
    type = models.ForeignKey(to=MembershipType, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(max_digits=5, decimal_places=2)
    payment_type = models.CharField(max_length=6, choices=PAYMENT_TYPE_CHOICES)
    payment_date = models.DateField()


class Member(models.Model):
    pass
