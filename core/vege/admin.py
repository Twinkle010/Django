from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'rank', 'total_marks', 'date_of_reportcard_generation', 'student_age']
    ordering = ['rank']

    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        return marks['marks']
    def student_age(self, obj):
        return obj.student.student_age
admin.site.register(ReportCard, ReportCardAdmin)