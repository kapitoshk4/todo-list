from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TagForm
from todo.models import Todo, Tag


class TodoListView(generic.ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todo_list"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")
