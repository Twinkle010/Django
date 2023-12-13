import random
from faker import Faker
fake = Faker()
from vege.models import *
from django.db.models import Sum

def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            department_objs = Department.objects.all()
            department_index = random.randint(0, len(department_objs)-1)
            department = department_objs[department_index]

            student_id = f"STU-0{random.randint(100,999)}"

            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(15,25)
            student_address = fake.address()

            studentid_objs = StudentID.objects.create(student_id=student_id)

            student_objs = Student.objects.create(
                department = department,
                student_id = studentid_objs,
                student_name = student_name,
                student_email =student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)

def create_subjectmarks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

def gen_reportcard():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', 'student_age') # studentmarks is the related name defined in subject marks model
    currentrank = -1
    i = 1
    # not an ideal option for more number of students
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            rank = i
        )
        i += 1