from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'


class Advisor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=100)
    contact = models.EmailField()


class Club(models.Model):
    slug = models.SlugField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_photo = models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/')
    advisor = models.ForeignKey(Advisor, null=True, on_delete=models.SET_NULL)
    contact = models.EmailField(null=True)
    description = models.TextField()


class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Event Types'

class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField(null=True)
    location = models.CharField(max_length=100)
