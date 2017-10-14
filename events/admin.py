from django.contrib import admin

from .models import Event
from .models import RecurringEvent

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'summary', 'start_date', 'end_date', 'category', 'event_site', 'image_url' ]
    list_display = ('title','start_date', 'end_date', 'category')

class RecurringEventAdmin(admin.ModelAdmin):
    fields = ['title', 'summary', 'website', 'image', 'days', 'isOnWeekend', 'startTime', 'endTime']
    list_display = ('title', 'summary')

admin.site.register(RecurringEvent, RecurringEventAdmin)
admin.site.register(Event, EventAdmin)
