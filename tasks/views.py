# Add all your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render

current_tasks = []
completed_tasks = []


def tasks_view(request):
    return render(request, "current.html", {"tasks": current_tasks})


def add_task_view(request):
    task_value = request.GET.get("task")
    current_tasks.append(task_value)
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, task_index):
    current_tasks.pop(task_index - 1)
    return HttpResponseRedirect("/tasks/")


def complete_task_view(request, task_index):
    task = current_tasks.pop(task_index - 1)
    completed_tasks.append(task)
    return HttpResponseRedirect("/tasks/")


def completed_task_view(request):
    return render(request, "completed.html", {"tasks": completed_tasks})


def all_tasks_view(request):
    return render(
        request, "all.html", {"current": current_tasks, "completed": completed_tasks}
    )
