from django.contrib import admin
import website.models as website_models

admin.site.site_header = "FKOC Administration"
admin.site.site_title = "FKOC Administration"
admin.site.index_title = "FKOC Administration"


@admin.register(website_models.BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "office_held"]
    list_display_links = ["last_name", "first_name"]
    list_filter = ["last_name", "first_name"]
    ordering = ["last_name", "first_name"]


@admin.register(website_models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "start_date", "end_date"]
    list_filter = ["name", "level", "start_date", "end_date"]
    ordering = ["start_date", "name"]


@admin.register(website_models.Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "email", "phone"]
    list_filter = ["last_name", "first_name", "email", "phone"]
    ordering = ["last_name", "first_name"]
