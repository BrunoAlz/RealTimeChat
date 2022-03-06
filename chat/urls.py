from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_index, name='chat_index'),
    path('Sala/<str:nome_sala>', views.sala_chat, name='sala_chat'),
]