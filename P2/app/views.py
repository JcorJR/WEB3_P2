from django.shortcuts import render, redirect

#Importes para o Usuario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Importes dos forms
from app.forms import FormUsuario

#Importe das models
from .models import Pagina, Produto, Contato

def index(request):
    pagina = Pagina.objects.first()
    produtos = Produto.objects.all()
    return render(request, 'index.html', {
        'pagina':pagina,
        'produtos':produtos})

#CRUD Usuário
@login_required(login_url='loginUsuario')
def dashboard(request):
    if not request.user:
        return redirect('loginUsuario')
    return render(request, "dashboar.html", {'usuario':request.user})

def loginUsuario(request):
    if request.POST:
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(request, username = nome , password = senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard.html')
        else:
            messages.error(request, "Usuário ou senha inválidos") 
    return render('login.html')

def cadastroUsuario(request):
    formulario = FormUsuario(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request, 'cadastro_usuario.html', {'form':formulario})

def logoutUsuario(request):
    logout(request)
    return redirect('loginUsuario')