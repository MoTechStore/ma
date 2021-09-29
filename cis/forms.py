from __future__ import unicode_literals
from django import forms
from .models import Task, Chat, User
from django.contrib.auth import get_user_model



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('supervisor', 'task_customer', 'task_desc', 'report', 'suspect', 'comment', 'modus')


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('message', )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')                
