# -*- coding: utf-8 -*-

from django import forms

from modelform.models import StudentRecord


class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = ('name', 'enrollment', 'faculty', 'year')

