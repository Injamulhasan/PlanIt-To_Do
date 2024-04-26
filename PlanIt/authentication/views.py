from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


def handlelogin(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            request.session['email'] = user.username
            messages.success(request, 'Sucessfully logged in')
            """if user.first_name == 'admin':
                return redirect('/admin_dash')"""
            return redirect(all_tasks)

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/')
   return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Sucessfully logged out')
    return redirect('/')# Create your views here.


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repeat = request.POST['repeat']
        if repeat == password:
            user = User.objects.create_user(username=email, password=password, first_name= firstname, last_name=lastname)
            return redirect('/')
        else:
            return redirect('/signup')

    return render(request, 'signup.html')

def all_tasks(request):
    todos = Task.objects.all()
    # print(type(todos[0].id))
    return render(request, 'all_task.html', {'todos': todos})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        Task.objects.create(task_name=task_name, category=category, priority=priority)
        return redirect('all_tasks')
def delete_todo(request,id):
    print(type(id))
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.delete()
    return render(request, 'all_task.html', {'todos': todos})
def change_status_pending(request,id):
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.status=False
    todo.save()
    return render(request, 'all_task.html', {'todos': todos})
def change_status_completed(request,id):
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.status=True
    todo.save()
    return render(request, 'all_task.html', {'todos': todos})

def weekly_task(request):
    # Fetch all tasks with priority set to "weekly"
    weekly_tasks = Task.objects.filter(priority='weekly')
    return render(request, 'weekly.html', {'weekly_tasks': weekly_tasks})

def monthly_task(request):
    # Fetch all tasks with priority set to "monthly"
    monthly_tasks = Task.objects.filter(priority='monthly')
    return render(request, 'monthly.html', {'monthly_tasks': monthly_tasks})

def completed_tasks(request):
    # Query the database to get completed tasks
    completed_tasks = Task.objects.filter(status=False)

    # Pass the completed tasks to the template
    return render(request, 'completed.html', {'completed_tasks': completed_tasks})


