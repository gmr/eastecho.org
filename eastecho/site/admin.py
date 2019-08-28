from django.contrib import admin

from . import models

admin.site.register(models.Advisor)
admin.site.register(models.Category)
admin.site.register(models.Club)
admin.site.register(models.Event)
admin.site.register(models.EventType)
