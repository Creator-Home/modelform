from rest_framework import viewsets

from modelform import serializers
from modelform.models import StudentRecord, CollegeRecord
import json
from django.db.models import Count

# q.prefetch_related('x___y___set').filter(x__y__isnull=False)


class StudentRecordViewset(viewsets.ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = serializers.StudentRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name',)
    extra_kwargs = {'url': {'lookup_field': 'name'}}

    # def get_queryset(self):
    #     data = self.filter_queryset(StudentRecord.objects.filter(id=4))
    #     return data
        # # data = self.queryset(StudentRecord.objects.values_list('name', 'enrollment', 'classname__name', 'classname__collegename__name'))
        # print(self.request.user)
        # data = self.filter_queryset(StudentRecord.objects
        #                              .all())
        # # data1 = json.dumps(list(self.filter_queryset(StudentRecord.objects
        # #                             .values('id','classname__name'))))
        # # print(data1)
        # # data = self.filter_queryset(StudentRecord.objects.values_list('name', 'enrollment', 'classname__name', 'classname__collegename__name'))
        # print(CollegeRecord.objects.all().prefetch_related('collegename__classname').filter(collegename__classname__isnull=False))
        # print(CollegeRecord.objects.prefetch_related('collegename').filter(collegename__isnull=True))
        # # print(CollegeRecord.objects.prefetch_related('collegename').filter(collegename__name__isnull=False).values_list('collegename__name'))
        # #
        # #
        # # print(CollegeRecord.objects.prefetch_related('collegename__classname').filter(collegename__classname__isnull=False, collegename__classname__name='bcjbd'))
        # # print(CollegeRecord.objects.prefetch_related('collegename__classname').values_list('collegename__classname__name'))
        # # data = self.filter_queryset(StudentRecord.objects.all())
        # # print(data)=self.request.user
        # # for i in data:
        # #     print(i)
        # # data = self.filter_queryset(StudentRecord.objects.annotate(Count('enrollment')))
        # # for i in data:
        # #     print(i.enrollment__count)
        #
        # return data
