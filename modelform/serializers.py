from rest_framework import serializers
from modelform import models

class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentRecord
        fields = ('id', 'name', 'enrollment', 'faculty', 'year', 'register_date', 'user')

class CustomRecordSerializer(serializers.Serializer):
    name = serializers.CharField()
    enrollment = serializers.CharField()

    class Meta:
        fields = ('name', 'enrollment',)

class PassedStudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    enrollment = serializers.IntegerField()
    year_of_passing = serializers.DateTimeField()

# CUSTOM SERIALIZER + ORM + SERIALIZER DISPLAY