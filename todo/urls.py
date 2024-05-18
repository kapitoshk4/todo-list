from django.urls import path
from todo.views import TodoListView, TagListView

urlpatterns = [
    path("", TodoListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
