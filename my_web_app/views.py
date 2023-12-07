from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def StudentRegister(request):
  form = StudentForm()
  if request.method == 'POST':
    form = StudentForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('')
    
  context = {'form':form}
  return render(request, 'register.html', context=context)

def studentView(request):
  
  record = Student.objects.all() # Getting the record with the help of a Student model
  
  context = {'record': record}
  return render(request, 'view.html', context=context)

def StudentUpdate(request, id):
 
  record = Student.objects.get(id=id) # Getting the record id with the help of a Student model
  form = StudentForm(instance=record)
    
  if request.method == 'POST':
    form = StudentForm(request.POST,instance=record)
    
    if form.is_valid():
      form.save()
    return redirect('')
  
  context = {'form':form}
  return render(request, 'register.html', context=context)

def StudentDelete(request, id):
  record = Student.objects.get(id=id) # Getting the record id with the help of a Student model
  record.delete()
  return redirect('')