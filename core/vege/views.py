from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recipe, Student, SubjectMarks
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .seed import *
from django.contrib.auth import get_user_model

# since already user model is being used here, define get user model to use custom user model 
User = get_user_model()


@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data= request.POST
        files = request.FILES.get('image')
        recipe_name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(name = recipe_name, description = description, recipe_image = files)
        
        return redirect('/recipes')
    querySet = Recipe.objects.all()

    if request.GET.get('search_re'):
        querySet = querySet.filter(name__icontains = request.GET.get('search_re'))
        # context = {'recipes': querySet}
        # return render(request, "recipes.html", context)

    context = {'recipes': querySet}
    return render(request, "recipes.html", context)

@login_required(login_url='/login/')
def delete_recipe(request, id):
    print(id)
    Recipe.objects.get(id=id).delete()
    return redirect('/recipes/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    # print(id)
    querySet = Recipe.objects.get(id=id)
    if request.method == "POST":
        data= request.POST
        querySet.image = request.FILES.get('image')
        querySet.name = data.get('name')
        querySet.description = data.get('description')
        querySet.save()
        return redirect('/recipes')

    context = {'recipe': querySet}
    return render(request, 'update_recipes.html', context)
    

def login_page(request):
    if request.method == "POST":
        user = User.objects.filter(username = request.POST.get('username'))
        if not user.exists():
            messages.error(request, "User doesn't exists, Please Register")
            return redirect('/register/')
        
        user_auth = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user_auth is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # success authenticate, add to session
            login(request, user_auth)
            return redirect('/recipes')

    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password) # password will be encrypted  by django
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('/register/')
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)
        )
    paginator = Paginator(queryset, 5) #show 25 items per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'students.html', {'queryset': page_obj})


def view_marks(request, student_id):
    # gen_reportcard()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', 'student_age') # studentmarks is the related name defined in subject marks model
    # currentrank = -1
    # i = 1
    # # not an ideal option for more number of students
    # for rank in ranks:
    #     if student_id == rank.student_id.student_id:
    #         currentrank = i
    #         break
    #     i += 1
    currentrank = ReportCard.objects.filter(student__student_id__student_id = student_id)[0].rank
    return render(request, 'view_marks.html', {'queryset': queryset, 'total_marks': total_marks, 'currentrank': currentrank})


