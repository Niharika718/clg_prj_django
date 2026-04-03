from django.shortcuts import render,redirect

# Create your views here.
from.models import student
from .forms import studentform

# read---------------------------------
def student_list(request):
    data=student.objects.all()
    return render(request,'student_list.html',{'data':data})

# create------------------------------
def add_student(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=studentform()

    return render(request,'student_form.html',{'form':form})

#update----------------------------------
def update_student(request,id):
    stu=student.objects.get(id=id)

    if request.method=='POST':
        form=studentform(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=studentform(instance=stu)
    return render(request,'student_form.html',{'form':form})

#delete-------------------------------------
def delete_student(request,id):
    stu=student.objects.get(id=id)
    stu.delete()
    return redirect('student_list')
