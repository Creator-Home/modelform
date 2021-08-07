from rest_framework import viewsets
from modelform import models
from modelform import serializers

class StudentRecordViewset(viewsets.ModelViewSet):
    queryset = models.StudentRecord.objects.all()
    serializer_class = serializers.StudentRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name', )
    extra_kwargs = {'url': {'lookup_field':'name'}}