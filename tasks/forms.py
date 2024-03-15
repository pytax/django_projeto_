from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status']
        

class TaskFormCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','due_date']