from django.contrib import admin

from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'start_date', 'end_date']
    list_display = ('title','start_date', 'end_date',)

admin.site.register(Event, EventAdmin)