from django.shortcuts import render
from .models import Teacher,Student
from .forms import TeacherForm,StudentForm
from django.shortcuts import get_object_or_404,redirect

def index(request):
    return render(request,'index.html')

def student_list(request):
    studentslist = Student.objects.filter(is_deleted=False)
    return render(request,'students_list.html',{'studentslist':studentslist})

def add_student(request):
    # fill form to user fornt end 

    if request.method == 'POST':
        form = StudentForm(request.POST)
     
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_list')
    else:
       
        # empty form
        form = StudentForm()
        teacherslist = Teacher.objects.values_list('id', 'class_teacher_name')
    return render(request,'addstudent.html',{'fomr':form,'teacherslist':teacherslist})

def edit_student(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
     
        form = StudentForm(request.POST,instance=student)
       
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
        teacherslist = Teacher.objects.values_list('id', 'class_teacher_name')
  

    return render(request,'addstudent.html',{'form':form,'teacherslist':teacherslist,'student':student})

def delete_student(request,student_id):
    student = get_object_or_404(Student, id=student_id)
    # if request.method == 'POST':
    student.delete()
    return redirect('student_list')

