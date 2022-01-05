from django.contrib import admin
import events.models as event_models


# Register your models here.
class EventDayTabularInline(admin.TabularInline):
    model = event_models.EventDate


@admin.register(event_models.Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventDayTabularInline]
    model = event_models.Event
    list_display = ["name", "first_day", "last_day"]


@admin.register(event_models.EventDocument)
class EventDocumentAdmin(admin.ModelAdmin):
    model = event_models.EventDocument
    list_display = ["event", "event_date", "title"]


@admin.register(event_models.EventLink)
class EventLinkAdmin(admin.ModelAdmin):
    model = event_models.EventLink
    list_display = ["event", "event_date", "title"]


class EventImageTabularInline(admin.TabularInline):
    model = event_models.EventImage


@admin.register(event_models.EventImageGallery)
class EventImageGalleryAdmin(admin.ModelAdmin):
    inlines = [EventImageTabularInline]
    model = event_models.EventImageGallery
    list_display = ["event", "event_date", "title"]
