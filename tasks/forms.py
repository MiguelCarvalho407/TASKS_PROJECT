from django.forms import ModelForm
from django import forms
from .models import Utilizadores, Task, Category


# ================================================== #

class SingupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput (attrs={
        'class':'form-control',
        'placeholder':'Nome completo'
    }))
    email = forms.EmailField(widget=forms.EmailInput (attrs={
        'class':'form-control',
        'placeholder':'exemplo@gmail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput (attrs={
        'class':'form-control',
        'placeholder':'**********'
    }))


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'exemplo@gmail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'**********'
    }))

# ================================================== #

class CriarTarefaForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'category']
        widgets = {
            'due_date':forms.DateInput (attrs={
                'class':'form-control',
                'type':'date'
            })
        }


class EditarTarefaForm(forms.Form):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'category']


class CriarCategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
