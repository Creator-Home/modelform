from django.shortcuts import render
from modelform.forms import StudentRecordForm

# Create your views here.
def modelform(request):
    if request.method == "POST":
        form_register = StudentRecordForm(request.POST)  #filled form
        if form_register.is_valid():
            form_register.save()

    return render(request, 'modelform/modelform.html',
                  {"StudentRecordForm": StudentRecordForm,},
                  )
