from django.contrib import admin
from django.urls import path, include

from todo.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "todo"
