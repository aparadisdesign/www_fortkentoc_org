from django.contrib import admin
import events.models as event_models
from django import forms
from django.db import models

# Register your models here.
class EventDayTabularInline(admin.TabularInline):
    model = event_models.EventDate


@admin.register(event_models.Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventDayTabularInline]
    model = event_models.Event
    list_display = ["name", "first_day", "last_day"]
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('https://cdn.ckeditor.com/4.17.1/standard/ckeditor.js',)


@admin.register(event_models.EventDocument)
class EventDocumentAdmin(admin.ModelAdmin):
    model = event_models.EventDocument
    list_display = ["event", "event_date", "title"]
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('https://cdn.ckeditor.com/4.17.1/standard/ckeditor.js',)


@admin.register(event_models.EventLink)
class EventLinkAdmin(admin.ModelAdmin):
    model = event_models.EventLink
    list_display = ["event", "event_date", "title"]
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('https://cdn.ckeditor.com/4.17.1/standard/ckeditor.js',)


class EventImageTabularInline(admin.TabularInline):
    model = event_models.EventImage


@admin.register(event_models.EventImageGallery)
class EventImageGalleryAdmin(admin.ModelAdmin):
    inlines = [EventImageTabularInline]
    model = event_models.EventImageGallery
    list_display = ["event", "event_date", "title"]
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('https://cdn.ckeditor.com/4.17.1/standard/ckeditor.js',)
