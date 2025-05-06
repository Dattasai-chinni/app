from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.list_students, name='list_students'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/', views.get_student, name='get_student'),
    path('students/<int:pk>/update/', views.update_student, name='update_student'),
    path('students/count/', views.total_student_count, name='total-student-count'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('students/names/', views.get_student_names, name='student-names'),
    path('students/search/', views.search_students_by_name, name='search_students_by_name'),

]
