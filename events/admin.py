from django.contrib import admin

from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['event_title', 'event_start_date', 'event_end_date']
    list_display = ('event_title','event_start_date', 'event_end_date',)

admin.site.register(Event, EventAdmin)