from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
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
