from django.db import models


# Create your models here.
class CollegeRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ClassRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)
    collegename = models.ForeignKey(CollegeRecord, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

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
    classname = models.ForeignKey(ClassRecord, on_delete=models.CASCADE, blank=True, null=True)




