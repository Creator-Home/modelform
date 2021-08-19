from django.shortcuts import render
from modelform.forms import StudentRecordForm
from modelform.models import StudentRecord, ClassRecord

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
