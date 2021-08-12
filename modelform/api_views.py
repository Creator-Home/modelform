from rest_framework import viewsets

from modelform import serializers
from modelform.models import StudentRecord
from django.db.models import Count

# q.prefetch_related('x___y___set').filter(x__y__isnull=False)


class StudentRecordViewset(viewsets.ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = serializers.StudentRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name',)
    extra_kwargs = {'url': {'lookup_field': 'name'}}

    def get_queryset(self):
        # data = self.filter_queryset(StudentRecord.objects
        #                             .filter(id=2)
        #                             .values_list('id', 'name'))
        data = self.filter_queryset(StudentRecord.objects.values_list('name', 'enrollment', 'classname__name', 'classname__collegename__name'))
        # data = self.filter_queryset(StudentRecord.objects.all())
        print(data)
        # for i in data:
        #     print(i)
        # data = self.filter_queryset(StudentRecord.objects.annotate(Count('enrollment')))
        # for i in data:
        #     print(i.enrollment__count)

        return data
