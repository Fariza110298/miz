from django.db import models

# Create your models here.
class Spec(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    sp_name = models.CharField(max_length=200, help_text="Enter a student spec")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.sp_name
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Student(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    st_name = models.CharField(max_length=200)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    GPA = models.TextField(max_length=1000, help_text="Enter a GPA of the student")
    iin = models.CharField('IIN',max_length=13, help_text='13 Character <a href="https://www.iin-international.org/content/what-iin">IIN number</a>')
    spec = models.ManyToManyField(Spec, help_text="Select a spec for this student")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.st_name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('student-detail', args=[str(self.id)])
import uuid # Required for unique student instances

class StudentInformation(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True) 
    mail = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Magistrant'),
        ('o', 'Otchislen'),
        ('a', 'Bakalavr'),
        ('r', 'Doctorant'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Student status')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.student.st_name)
class Teacher(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_hire = models.DateField('Hire', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('teacher-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)