from django.db import models
from django.urls import reverse
from utils.constants import *
from django.contrib.auth.models import User

class Todo(models.Model):
    titulo = models.CharField(
        'Titulo',
        max_length=200  
    )

    conteudo = models.CharField(
        'Conteudo',
        max_length=500  
    )

    cor = models.CharField(
        max_length=15,
        choices=COR_DO_TODO,
        default=PRIMARYY,
    )

    datacadastro = models.DateTimeField(
        'Criado em:',
        auto_now_add=True,
        auto_now=False
    )

    datamodificacao = models.DateTimeField(
        'Modificado em:',
        auto_now_add=False,
        auto_now=True
    )

    is_done = models.BooleanField(
        default=False
    )

    like = models.ManyToManyField(
        User,
        verbose_name='Usuário',
        related_name='users',       
        blank=True,        
    )
    

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
