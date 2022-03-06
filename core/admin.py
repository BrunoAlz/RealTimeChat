from django.contrib import admin

from core.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'conteudo', 'cor',]


