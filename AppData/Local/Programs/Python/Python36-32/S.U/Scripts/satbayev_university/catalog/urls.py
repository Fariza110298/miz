from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
]