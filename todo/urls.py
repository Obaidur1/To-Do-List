from django.urls import path
from .views import (
    Show_Task,
    Add_Task,
    Delete_Task,
    Edit_Task,
    Completed_Task,
    Complete_Task,
)

urlpatterns = [
    path("", Show_Task.as_view(), name="show_task"),
    path("add-task", Add_Task.as_view(), name="add_task"),
    path("delete/<int:pk>", Delete_Task.as_view(), name="delete_task"),
    path("edit/<int:pk>", Edit_Task.as_view(), name="edit_task"),
    path("complete/<int:pk>", Complete_Task.as_view(), name="complete"),
    path("completed-tasks", Completed_Task.as_view(), name="completed_task"),
]
