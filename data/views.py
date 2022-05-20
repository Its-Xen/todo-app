from django.shortcuts import render

from .models import todo

def home(request):
    task = todo.objects.all()
    context = {"task" : task}
    return render(request, "home.html", context)