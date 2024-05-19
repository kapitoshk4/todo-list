from django import forms

from todo.models import Tag, Todo


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title", ]


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline", "tags"]

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date"
        }),
        required=False
    )
