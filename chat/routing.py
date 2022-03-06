from django.urls import re_path

from .comsumers import ChatConsumer

"""
Iniciamos a Url com o WS que vem de WebSockets
Pegaremos o Nome da Sala após o Chat/ com a RE
"""
websocket_urlpatterns = [
    re_path(r'ws/Chat/(?P<nome_sala>\w+)/$', ChatConsumer)

]