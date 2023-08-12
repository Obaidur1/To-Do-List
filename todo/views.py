from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, CreateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import TaskModelForm
from .models import TaskModel
from django.urls import reverse_lazy
from django.views import View


# Create your views here.
class Show_Task(ListView):
    model = TaskModel
    template_name = "show_tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)


class Add_Task(CreateView):
    model = TaskModel
    template_name = "add_task.html"
    form_class = TaskModelForm
    success_url = reverse_lazy("show_task")


class Delete_Task(DeleteView):
    model = TaskModel
    template_name = "delete_task.html"
    success_url = reverse_lazy("show_task")


class Edit_Task(UpdateView):
    model = TaskModel
    template_name = "edit_task.html"
    form_class = TaskModelForm
    success_url = reverse_lazy("show_task")


class Complete_Task(View):
    def get(self, request, pk):
        task = TaskModel.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return redirect("completed_task")


class Completed_Task(ListView):
    model = TaskModel
    template_name = "completed_task.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)
