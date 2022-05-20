from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todo

def home(request):
    task = todo.objects.all()
    context = {"task" : task}
    return render(request, "home.html", context)


def Add(request):
    new_item = todo(task = request.POST['task'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delete(request, pk):
    del_item = todo.objects.get(id = pk)
    del_item.delete()
    return HttpResponseRedirect('/todo/')
