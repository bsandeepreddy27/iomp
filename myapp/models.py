# myapp/models.py

from django.db import models
import datetime

class Judge(models.Model):
    name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, default='Unknown')
    date_of_appointment = models.DateField(default=datetime.date(2000, 1, 1))
    becomes_cji_on = models.DateField(null=True, blank=True)
    date_of_retirement = models.DateField(default=datetime.date(2000, 1, 1))
    tenure_length = models.CharField(max_length=50, default='')
    tenure_length_as_cji = models.CharField(max_length=50, null=True, blank=True)
    parent_high_court = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name




class Case(models.Model):
    CATEGORY_CHOICES = [
        ('CR', 'Criminal'),
        ('CV', 'Civil'),
        ('FA', 'Family'),
        ('PR', 'Property'),
        ('LA', 'Labor'),
        ('IN', 'Intellectual Property'),
    ]

    name = models.CharField(max_length=255)
    judge = models.ForeignKey('Judge', on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    estimated_time_to_close = models.DurationField()

    def __str__(self):
        return self.name


