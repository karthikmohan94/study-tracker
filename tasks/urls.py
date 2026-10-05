from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="list"),
    path("<int:task_id>/toggle/", views.toggle_task, name="toggle"),
    path("<int:task_id>/delete/", views.delete_task, name="delete"),
]