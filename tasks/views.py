from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import TaskForm
from .models import Task

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:list")
    else:
        form = TaskForm()

    tasks = Task.objects.order_by("-id")

    return render(request, "tasks/task_list.html", {
        "form": form,
        "tasks": tasks,
    })
    
    
    
@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("tasks:list")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("tasks:list")