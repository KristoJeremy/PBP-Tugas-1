from django import forms
from todolist.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=255)