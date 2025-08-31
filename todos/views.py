from django.shortcuts import render , get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

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


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        context = {
            'form': form,
        }
        return render(request,'todos/task_form.html',context)

def task_update(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail',pk=task.pk)
    else:
        form = TaskForm(instance=task)
        context = {
            'form': form,
            'task': task,        
            }
        return render(request,'todos/task_form.html',context)

def task_delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    context = {
        'task': task
    }

    return render(request,'todos/task_confirm_delete.html',context)
