from django.shortcuts import render
from django.views import generic

from todo.models import Todo


class TodoListView(generic.ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todo-list"
