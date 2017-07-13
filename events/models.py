from django.db import models

# Create your models here.

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_start_date = models.DateTimeField('start date')
    event_end_date = models.DateTimeField('end date')
    