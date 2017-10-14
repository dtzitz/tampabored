from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(default='Hodor') 
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    event_site = models.URLField(default='#')
    image_url = models.URLField(default='https://res.cloudinary.com/dtzitz/image/upload/v1467560008/AOjKtQy_jxytxw.jpg')
    category = models.CharField(
        max_length = 50,
        choices = (
            ('Concert', 'CON'),
            ('Festival', 'FEST'),
            ('Kids', 'KIDS'),
            ('Miscellaneous', 'MISC')
        ),
        default = 'Miscellaneous'
    )

class RecurringEvent(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(default='100 char max', max_length=100)
    website = models.URLField(default='#')
    image = models.URLField(default='#')
    days = models.CharField(max_length=25)
    isOnWeekend = models.BooleanField(default=True)
    startTime = models.TimeField
    endTime = models.TimeField
    