from django.core.management.base import BaseCommand, CommandError
from membership.models import MembershipType, Membership, Member
from website.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        for member in Member.objects.all():
            member.state = member.state.replace(f" {member.postal_code}", "")
            member.save()

