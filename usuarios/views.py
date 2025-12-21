from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        Usuario.objects.create(
            email=email,
            senha=senha,
            perfil='estagiario'
        )

        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
         # Verifica se o email existe no banco de dados
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
             return redirect('/cadastro/') # email não existe → cadastro

        if usuario.senha != senha:
            return render(request, 'usuarios/login.html',
                {'erro': 'Senha incorreta.'})
        
         # Login correto
        #request.session['usuario_id'] = usuario.id
        request.session['email'] = usuario.email
        return redirect('/home/')

def logout(request):
    request.session.flush()  # limpa a sessão
    return redirect('/login/')