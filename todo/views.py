from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class IndexListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class IndexCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class IndexUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class IndexDeleteView(generic.DeleteView):
    model = Task
    success_url = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def change_readiness(request, pk):
    task = Task.objects.get(id=pk)
    task.readiness = not task.readiness
    task.save()
    return redirect("todo:index")
