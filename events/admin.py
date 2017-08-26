from django.contrib import admin

from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'summary', 'start_date', 'end_date', 'category', 'event_site', 'image_url' ]
    list_display = ('title','start_date', 'end_date', 'category')

admin.site.register(Event, EventAdmin)