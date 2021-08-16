from django.db import models
from django.conf import settings

# Create your models here.
class CollegeRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
    #     db_table = 'collegerecord'
        verbose_name = 'College Record'
        verbose_name_plural = 'College Record'

class ClassRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)
    collegename = models.ForeignKey(CollegeRecord, on_delete=models.CASCADE, blank=True, null=True, related_name="collegename")

    def __str__(self):
        return self.name

    class Meta:
    #     db_table = 'classrecord'
        verbose_name = 'Class Record'
        verbose_name_plural = 'Class Record'

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
    classname = models.ForeignKey(ClassRecord, on_delete=models.CASCADE, blank=True, null=True, related_name="classname")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)


    class Meta:
    #     db_table = 'studentrecord'
        verbose_name = 'Student Record'
        verbose_name_plural = 'Student Record'




