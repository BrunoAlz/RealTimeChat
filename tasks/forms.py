from django import forms

from utils.constants import COR_DO_TODO
from .models import Tasks


class TaskForm(forms.ModelForm):    
    titulo = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titulo do TODO',            
        })        
)

    conteudo = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Conteúdo',

        })

) 

    cor = forms.ChoiceField(
        choices=COR_DO_TODO,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select text-center',
            'placeholder': 'Selecione uma Categoria',
        })
    )

    class Meta:
        model = Tasks
        fields = ['titulo', 'conteudo', 'cor',]