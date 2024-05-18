from django import forms

from todo.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title", ]
