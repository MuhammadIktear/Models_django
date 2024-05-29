from django.shortcuts import render, redirect
from . import models
from model_app.forms import StudentForm

# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request, 'home.html', {'student': student})

def delStudent(request, roll):
    models.Student.objects.get(pk=roll).delete()
    return redirect('home')

def student(request):
    message = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Add student successfully'
    else:
        form = StudentForm()
    
    return render(request, 'form.html', {'form': form, 'message': message})


