from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import IndexForm
from todo.models import Tag, Task


class IndexListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    paginate_by = 3


class IndexCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class = IndexForm


class IndexUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class = IndexForm


class IndexDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


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
