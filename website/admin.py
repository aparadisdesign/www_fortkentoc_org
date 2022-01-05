from django.contrib import admin
import website.models as website_models


@admin.register(website_models.BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'office_held']
    list_display_links = ['last_name', 'first_name']
    list_filter = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


@admin.register(website_models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'start_date', 'end_date']
    list_filter = ['name', 'level', 'start_date', 'end_date']
    ordering = ['start_date', 'name']