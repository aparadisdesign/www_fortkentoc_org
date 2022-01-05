from django.contrib import admin
from .models import MembershipType, Membership, Member
from website.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'last_login', 'is_active', 'is_staff']


@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'price']
    list_display_links = None
    list_filter = ['name', 'year']
    ordering = ['-year', 'name']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'address', 'city', 'state', 'postal_code', 'user']
    list_filter = ['last_name', 'first_name', 'address', 'city', 'state', 'postal_code']
    ordering = ['last_name', 'first_name']


class MemberTabularInline(admin.TabularInline):
    model = Member


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    inlines = [MemberTabularInline]
    model = Membership
    list_display = ('uuid', 'type', 'amount_paid', 'payment_type', 'payment_date')
