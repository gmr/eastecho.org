import autoslug
from ckeditor import fields
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = autoslug.AutoSlugField(populate_from='name', unique=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Advisor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    room = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = autoslug.AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, null=True, on_delete=models.SET_NULL)
    contact_email = models.EmailField(blank=True, null=True)
    president = models.CharField(blank=True, null=True, max_length=200)
    vice_president = models.CharField(blank=True, null=True, max_length=200)
    treasurer = models.CharField(blank=True, null=True, max_length=200)
    secretary = models.CharField(blank=True, null=True, max_length=200)
    icon = models.CharField(max_length=30, default='fas fa-user-friends')
    cover_photo = models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')
    description = fields.RichTextField()

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=200, unique=True)
    this_week_lead = models.TextField(null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Event Type'
        verbose_name_plural = 'Event Types'

    def __str__(self):
        return self.name


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100)
    notes = fields.RichTextField(null=True)

    class Meta:
        ordering = ['start_at', 'club', 'event_type']

    def __str__(self):
        return '{} - {} {}'.format(
            self.start_at.strftime('%Y-%m-%d %I:%M %p'),
            self.club.name, self.event_type.name)
