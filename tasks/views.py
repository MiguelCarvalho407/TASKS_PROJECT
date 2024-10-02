from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SingupForm, LoginForm, CriarTarefaForm
from .models import Utilizadores, Task
from django.contrib import messages

def base(request):
    return render(request, 'base.html')

def custom_404(request, exception):
    return render(request, 'error/404.html', status=404)

# ================================================== #

def signup_view(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():

            Utilizadores.objects.create_user(
                username =form.cleaned_data['username'],
                email =form.cleaned_data['email'],
                password =form.cleaned_data['password'],
            )

            return redirect('login')
    else:
        form = SingupForm()

    return render(request, 'registration/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('app')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('base')

# ================================================== #

@login_required
def app(request):
    return render(request, 'app/app.html')


@login_required
def criartarefa(request):
    if request.method == 'POST':
        form = CriarTarefaForm(request.POST or None)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, "Tarefa criada com sucesso!")
            return redirect('listatarefas')
    else:
        form = CriarTarefaForm()
        
    return render(request, 'app/criar_tarefa.html', {'form':form})


@login_required
def editartarefa(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = CriarTarefaForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('listatarefas')
    else:
        form = CriarTarefaForm(instance=task)
    return render(request, 'app/editar_tarefa.html', {'form':form})


@login_required
def listatarefas(request):
    tasks = Task.objects.filter(user=request.user) # FILTRA AS TAREFAS POR UTILIZADOR, PARA NÃO APARECERAM AS MESMAS TAREFAS PARA TODOS OS UTILIZADORES
    return render(request, 'app/lista_tarefas.html', {'tasks':tasks})


@login_required
def apagartarefa(request, pk):
    task = Task.objects.filter(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('listatarefas')
    return render(request, 'app/apagar_tarefa.html', {'task':task})

