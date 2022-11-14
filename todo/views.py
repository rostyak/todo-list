from django.shortcuts import render
from django.views import generic

from todo.models import Tag


def index(request):
    return render(request, "todo/index.html")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
