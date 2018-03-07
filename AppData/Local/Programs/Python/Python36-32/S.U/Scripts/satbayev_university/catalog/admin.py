from django.contrib import admin

# Register your models here.
from .models import Teacher, Spec, Student, StudentInformation

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Spec)
admin.site.register(StudentInformation)