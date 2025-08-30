from django.shortcuts import render , get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'todos/task_list.html', context)

def task_detail(request,pk):
    task = get_object_or_404(Task,pk=pk)
    context = {
        'task': task
    }
    return render(request,'todos/task_detail.html',context)

