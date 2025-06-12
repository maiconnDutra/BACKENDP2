from django.shortcuts import render
from todos.models import Todo
from django.views.generic import ListView

# Create your views here.
class TodoListView(ListView):
    model = Todo