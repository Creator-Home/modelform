from django.contrib import admin

from modelform.models import StudentRecord, ClassRecord, CollegeRecord


# Register your models here.

class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'faculty', 'year', 'register_date', 'classname', 'user')
    search_fields = ('name', 'enrollment', 'faculty', 'year', 'register_date')


admin.site.register(StudentRecord, StudentRecordAdmin)


class ClassRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'collegename', 'register_date')
    search_fields = ('name', 'register_date')


admin.site.register(ClassRecord, ClassRecordAdmin)

class CollegeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'register_date')
    search_fields = ('name', 'register_date')


admin.site.register(CollegeRecord, CollegeRecordAdmin)