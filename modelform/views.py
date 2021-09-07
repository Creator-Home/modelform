from django.shortcuts import render
from modelform.forms import StudentRecordForm
from modelform.models import StudentRecord, ClassRecord
from rest_framework import viewsets
from rest_framework import mixins
from modelform.serializers import CustomRecordSerializer, PassedStudentSerializer

# Create your views here.
def modelform(request):
    if request.method == "POST":
        form_register = StudentRecordForm(request.POST)  #filled form
        if form_register.is_valid():
            form_register.save()

    return render(request, 'modelform/modelform.html',
                  {"StudentRecordForm": StudentRecordForm,},
                  )

def blog(request):
    return render(request, 'blog/index.html')


def ecommerce(request):
    ls = StudentRecord.objects.all()
    cr = ClassRecord.objects.all()
    return render(request, 'ecommerce/index.html', {'record':ls, 'cr':cr})


class CustomStatusViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin):
    """
    APIs for list and retrieve Camera Status from rtsp_url
    """
    serializer_class = CustomRecordSerializer

    def get_queryset(self):
        """
        Overriding get_queryset to query the database to get the camera status info from rtsp_url
        :return: Queryset with camera status detail
        """
        student_ls = list(StudentRecord.objects.all().values('name', 'enrollment'))
        return student_ls


class StudentStatusViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = PassedStudentSerializer

    def get_queryset(self):
        student_ls = list(StudentRecord.objects.all().filter(enrollment__lte = 6).values('name', 'enrollment', 'register_date'))

        for student in student_ls:
            student['year_of_passing'] = student['register_date']

        return student_ls


# CreateModelMixin --> post
# RetrieveModelMixin --> particular record
# UpdateModelMixin --> put
# DestroyModelMixin --> delete