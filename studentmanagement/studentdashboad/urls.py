from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list,name="student_list"),
    path('addstudent/',views.add_student,name="add_student"),
    path('<int:student_id>/editstudent/',views.edit_student,name="edit_student"),
    path('<int:student_id>/deletestudent/',views.delete_student,name="delete_student"),
]