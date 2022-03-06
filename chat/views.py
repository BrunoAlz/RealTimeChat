from django.shortcuts import render

def chat_index(request):
    template = 'chat/chat_index.html'
    
    context = {        

    }
    return render(request, template, context)