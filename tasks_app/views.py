
from django.shortcuts import render
from .models import Task

def task_inbox(request):
    tasks = Task.objects.filter(completed=False).order_by('-created_at')
    return render(request, 'tasks_app/task_inbox.html', {'tasks': tasks})

def task_today(request):
    from datetime import date
    today = date.today()
    tasks = Task.objects.filter(due_date__date=today, completed=False)
    return render(request, 'tasks_app/task_today.html', {'tasks': tasks})

def task_upcoming(request):
    from datetime import date
    today = date.today()
    tasks = Task.objects.filter(due_date__gt=today, completed=False)
    return render(request, 'tasks_app/task_upcoming.html', {'tasks': tasks})



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_app/task_list.html', {'tasks': tasks})

from django.shortcuts import get_object_or_404, redirect
from .forms import TaskForm

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks_app/task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks_app/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks_app/task_confirm_delete.html', {'task': task})

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True).order_by('-due_date')
    return render(request, 'tasks_app/completed_tasks.html', {'tasks': tasks})
