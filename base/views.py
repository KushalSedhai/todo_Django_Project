from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def home(request):
    todo_objs= Todo.objects.all()
    return render(request, 'index.html', context={'todos':todo_objs})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status= request.POST.get('status')
        Todo.objects.create(name=name, description=description, status =status)
        return redirect('home')
    return render(request, 'create.html')

def edit(request, pk):
    todo_objs = Todo.objects.get(id=pk)
    
    if request.method == 'POST':
        todo_objs.name = request.POST.get('name')
        todo_objs.description = request.POST.get('description')
        todo_objs.status = request.POST.get('status')
        todo_objs.save()
        return redirect('home')
    return render(request, 'edit.html', context={'todo':todo_objs})

def delete(request, pk):
    todo_objs = Todo.objects.get(id=pk)
    todo_objs.delete()
    return redirect('home')

def deleteall(request):
    # Todo.objects.delete()
    return render(request, 'delete.html')

def deletingall(request):
    todo_objs = Todo.objects.all()
    todo_objs.delete()
    return redirect('home')