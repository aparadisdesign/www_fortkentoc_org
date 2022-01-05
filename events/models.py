from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=65, null=False, blank=False)
    slug = models.SlugField()
    event_banner_image = models.ImageField(
        upload_to="uploads/events/banners/% Y/% m/% d/", null=True, blank=True
    )
    description = models.TextField()
    event_pdf = models.FileField(
        upload_to="uploads/events/pdfs/% Y/% m/% d/", null=True, blank=True
    )

    def __str__(self):
        return self.name

    @property
    def first_day(self):
        return self.eventdate_set.order_by("event_date").first().event_date

    @property
    def last_day(self):
        return self.eventdate_set.order_by("event_date").last().event_date

    class Meta:
        ordering = ["name"]
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventDate(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    event_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.event_date.__str__()

    class Meta:
        ordering = ["event_date"]
        verbose_name = "Event Date"
        verbose_name_plural = "Event Dates"


class EventDocument(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    event_date = models.ForeignKey(
        to=EventDate, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=65)
    description = models.TextField()
    document = models.FileField(
        upload_to="uploads/events/docs/% Y/% m/% d/", null=False, blank=False
    )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ["event", "event_date", "title"]
        verbose_name = "Event Document"
        verbose_name_plural = "Event Documents"


class EventLink(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    event_date = models.ForeignKey(
        to=EventDate, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=65)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ["event", "event_date", "title"]
        verbose_name = "Event Link"
        verbose_name_plural = "Event Links"


class EventImageGallery(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    event_date = models.ForeignKey(
        to=EventDate, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=65)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["event", "title"]
        verbose_name = "Event Gallery"
        verbose_name_plural = "Event Galleries"


class EventImage(models.Model):
    gallery = models.ForeignKey(to=EventImageGallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/events/images/% Y/% m/% d/")
    caption = models.CharField(max_length=255)
