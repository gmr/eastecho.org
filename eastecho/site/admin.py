from django.contrib import admin

from . import models


class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'email']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['slug', 'name']


class ClubAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']


admin.site.register(models.Advisor, AdvisorAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Club, ClubAdmin)
admin.site.register(models.Event)
admin.site.register(models.EventType)
