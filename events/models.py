from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(default='Hodor') 
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
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
