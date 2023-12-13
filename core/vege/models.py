from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    view_count = models.IntegerField(null=True, blank=True)


class Department(models.Model):
    department = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department'] # order based on department

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Subject(models.Model):
    subject_name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    # foregin key because manyto one or one to many relationship, many students can belong to a department or a department can have many students 
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    # one to one relation because a student can have only one id 
    student_name = models.CharField(max_length=20)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    # now everything wherever we use Recipe.objects.all(), need to change the expression saying Recipe.objects.filter(is_deleted=False)
    # so change model manager

    #objects is the default model manager
    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name


    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}:{self.marks}"
    
    class Meta:
        unique_together = ['student', 'subject']

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentrank", on_delete=models.CASCADE) # related name used to refer back to student model from this object
    # refer to view_marks.html 
    # rverse relation from this model(ReportCard) back to the ref model(Student) 
    rank = models.IntegerField()
    date_of_reportcard_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['rank', 'date_of_reportcard_generation']


# signals
# any kinda hint for any activiyt
# pre_save, post_save, pre_delete, post_delete