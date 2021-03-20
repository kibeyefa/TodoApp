from django import forms
from django.forms import ModelForm
from .models import Task


class MyForm(ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Enter a task"}))

    class Meta:
        model = Task
        fields = ["title"]