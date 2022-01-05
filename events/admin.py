from django.contrib import admin
import events.models as event_models


# Register your models here.
class EventDayTabularInline(admin.TabularInline):
    model = event_models.EventDate


@admin.register(event_models.Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventDayTabularInline]
    model = event_models.Event
    list_display = ['name', 'first_day', 'last_day']