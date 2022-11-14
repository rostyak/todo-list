from django.contrib import admin
from django.urls import path, include

from todo.views import index, TagListView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list")
]

app_name = "todo"
