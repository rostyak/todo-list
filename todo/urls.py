from django.urls import path

from todo.views import (
    IndexListView,
    IndexCreateView,
    IndexUpdateView,
    IndexDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, change_readiness,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("create/", IndexCreateView.as_view(), name="index-create"),
    path("<int:pk>/update/", IndexUpdateView.as_view(), name="index-update"),
    path("<int:pk>/delete/", IndexDeleteView.as_view(), name="index-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/change-readiness/", change_readiness, name="change-readiness")
]

app_name = "todo"
