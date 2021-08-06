from django.db import models


# Create your models here.

class StudentRecord(models.Model):
    CHOICES = (('None', 'None'),
               ('first', 'First'),
               ('second', 'Second'),
               ('third', 'Third'),
               ('forth', 'Forth')
               )
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    enrollment = models.IntegerField(blank=True, null=True)
    faculty = models.CharField(max_length=255, blank=False, null=False, default='None')
    year = models.CharField(max_length=255, blank=False, null=False, default='None', choices=CHOICES)
    register_date = models.DateTimeField(auto_now_add=True)

