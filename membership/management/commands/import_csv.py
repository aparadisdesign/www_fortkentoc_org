from django.core.management.base import BaseCommand, CommandError
from membership.models import MembershipType, Membership, Member
from website.models import User
import csv
import datetime
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("./members.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'x' and row[5] == 'Family':
                    membership = Membership()
                    membership.type = MembershipType.objects.get(name="Family", year="2022")
                    if row[10] == 'gratis':
                        membership.amount_paid = 0
                    elif row[10] == '$60.00':
                        membership.amount_paid = 60
                    else:
                        membership.amount_paid = 60
                    if row[2] == 'snowshoe raffle':
                        membership.payment_type = "Gratis"
                    if row[2] == 'pp' or row[2] == 'PP':
                        membership.payment_type = "Paypal"
                    if row[2] == 'cash':
                        membership.payment_type = "Cash"
                    if row[2] == 'check':
                        membership.payment_type = "Check"
                    membership.payment_date = datetime.datetime.strptime(row[1], '%M/%d/%Y')
                    #membership.save()
                    member = Member()
                    member.membership = membership
                    member.first_name = row[4]
                    member.last_name = row[3]
                    member.address = row[6]
                    member.city = row[7].split(", ")[0]
                    member.state = row[7].split(", ")[1]
                    if row[9] != '':
                        try:
                            member.user = User(email=row[9], is_staff=False, is_superuser=False, is_active=False).save()
                        except IntegrityError:
                            if User.objects.get(email=row[9]):
                                member.user = User.objects.get(email=row[9])
                    #member.save()

