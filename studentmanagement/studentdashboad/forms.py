from django import forms
from .models import Teacher,Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['class_teacher_name','email']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','class_teacher','class_name','admission_date','yearly_fees','is_deleted']
