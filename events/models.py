from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=65, null=False, blank=False)
    slug = models.SlugField()
    description = models.TextField()
    event_pdf = models.FileField(upload_to="uploads/events/pdfs/% Y/% m/% d/", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def first_day(self):
        return self.eventdate_set.order_by('event_date').first().event_date

    @property
    def last_day(self):
        return self.eventdate_set.order_by('event_date').last().event_date


class EventDate(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    event_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=True, blank=True)