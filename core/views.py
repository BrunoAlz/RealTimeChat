from re import template
from django.shortcuts import get_object_or_404, render
from core.forms import TodoForm

from core.models import Todo


def index(request):
    template = 'core/index.html'
    todos = Todo.objects.all()
    form = TodoForm()
    context = {        
        'form': form,
        'todos': todos,
    }
    return render(request, template, context)

def add_task(request):
    template =  'core/list_task.html'
    todos = Todo.objects.all()

    titulo = request.POST.get('titulo')
    conteudo = request.POST.get('conteudo')
    cor = request.POST.get('cor')

    task = Todo.objects.create(
        titulo=titulo, 
        conteudo=conteudo, 
        cor=cor
        )
    task.save()

    context = {
        'todos': todos,
    }
    return render(request, template, context)

def del_task(request, id):
    template = 'core/list_task.html'
    task = Todo.objects.get(id=id)
    task.delete()    

    todos = Todo.objects.all()

    context = {
    'todos': todos,
    }
    
    return render(request, template, context)

def like(request, id):
    template = 'core/list_task.html'
    task = Todo.objects.get(id=id)
    
    if task.like.filter(id=request.user.id).exists():
        task.like.remove(request.user)
    else:
        task.like.add(request.user)  

    todos = Todo.objects.all()
    
    context = {
    'todos': todos,

    }
    
    return render(request, template, context)


def search_task(request):
    template = 'core/search_result.html'
    query_text = request.POST.get('query')

    print(query_text)   

    results = Todo.objects.filter(
        titulo__icontains=query_text
        )
        

    print(results)
    context = {
        'results': results
    }
    return render(request, template, context)