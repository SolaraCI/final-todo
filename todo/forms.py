from .models import Task
from django import forms
from django.forms import ModelForm


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task'}), label="")
    class Meta:
        model = Task
        fields = ['name', 'notes', 'progress', 'importance']