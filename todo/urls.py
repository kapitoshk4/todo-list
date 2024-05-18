from django.urls import path
from todo.views import TodoListView, TagListView, TagCreateView, TagUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update")
]

app_name = "todo"
