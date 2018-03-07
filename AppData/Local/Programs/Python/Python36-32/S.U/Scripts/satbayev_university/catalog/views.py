from django.shortcuts import render

# Create your views here.
from .models import Student, Teacher, StudentInformation, Spec

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_students=Student.objects.all().count()
    num_informations=StudentInformation.objects.all().count()
    # Available books (status = 'a')
    num_informations_available=StudentInformation.objects.filter(status__exact='a').count()
    num_teachers=Teacher.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_students':num_students,'num_informations':num_informations,'num_informations_available':num_informations_available,'num_teachers':num_teachers},
    )
from django.views import generic

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2
class StudentDetailView(generic.DetailView):
    model = Student
from django.views import generic

class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 2
class TeacherDetailView(generic.DetailView):
    model = Teacher