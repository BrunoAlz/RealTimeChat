from django.shortcuts import render
from tasks.forms import TaskForm
from tasks.models import Tasks


def tasks_index(request):
    template = 'tasksT/tasks_index.html'
    tasks = Tasks.objects.all()
    form = TaskForm()
    context = {        
        'form': form,
        'tasks': tasks,
    }
    return render(request, template, context)

def add_task(request):
    template =  'tasksT/list_task.html'
    tasks = Tasks.objects.all()

    titulo = request.POST.get('titulo')
    conteudo = request.POST.get('conteudo')
    cor = request.POST.get('cor')

    task = Tasks.objects.create(
        titulo=titulo, 
        conteudo=conteudo, 
        cor=cor
        )
    task.save()

    context = {
        'tasks': tasks,
    }
    return render(request, template, context)

def del_task(request, id):
    template = 'tasksT/list_task.html'
    task = Tasks.objects.get(id=id)
    task.delete()    

    tasks = Tasks.objects.all()

    context = {
    'tasks': tasks,
    }
    
    return render(request, template, context)

def like(request, id):
    template = 'tasksT/list_task.html'
    task = Tasks.objects.get(id=id)
    
    if task.like.filter(id=request.user.id).exists():
        task.like.remove(request.user)
    else:
        task.like.add(request.user)  

    tasks = Tasks.objects.all()
    
    context = {
    'tasks': tasks,

    }
    
    return render(request, template, context)


def search_task(request):
    template = 'tasksT/search_result.html'
    query_text = request.POST.get('query')

    print(query_text)   

    results = Tasks.objects.filter(
        titulo__icontains=query_text
        )        

    print(results)
    context = {
        'results': results
    }
    return render(request, template, context)