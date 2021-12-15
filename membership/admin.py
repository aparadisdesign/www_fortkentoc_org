from django.contrib import admin
from .models import MembershipType, Membership, Member


@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'price']
    list_display_links = None
    list_filter = ['name', 'year']
    ordering = ['-year', 'name']


class MemberTabularInline(admin.TabularInline):
    model = Member


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    inlines = [MemberTabularInline]
    model = Membership
    list_display = ('uuid', 'type', 'amount_paid', 'payment_type', 'payment_date')
