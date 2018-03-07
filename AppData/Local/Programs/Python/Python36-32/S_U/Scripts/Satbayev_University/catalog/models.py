from django.db import models

# Create your models here.
class Specialty(models.Model):
    """
    Model representing a student specialty (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a student specialty  (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Student(models.Model):
    """
    Model 
    """
    student_name = models.CharField(max_length=200)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    ball = models.TextField(max_length=1000, help_text='Enter a ball of the student')
    iin = models.CharField('IIN',max_length=13, help_text='13 Character <a href="https://www.iin-international.org/content/what-iin">IIN number</a>')
    specialty = models.ManyToManyField(Specialty, help_text='Select a specialty for this student')
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.student_name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this student.
        """
        return reverse('student-detail', args=[str(self.id)])
import uuid # Required for unique student informations

class StudentInformation(models.Model):
    """
    Model representing a specific copy of a student (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular student across whole library")
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True) 
    mail = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Magistrant'),
        ('o', 'Otchislen'),
        ('a', 'Bakalavr'),
        ('r', 'Doctorant'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Student status')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.book.title)
class Teacher(models.Model):
    """
    Model representing an teacher.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_hire = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular.
        """
        return reverse('teacher-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)