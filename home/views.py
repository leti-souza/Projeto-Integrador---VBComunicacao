from urllib import request 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario 


def home(request):
    return render(request, 'home/home.html')


def noticias(request):
    
    noticias_fake = [
        {
            'titulo': 'Chuvas intensas atingem o sertão da Paraíba',
            'data': '10/12/2025',
            'fonte': 'G1 Paraíba'
        },
        {
            'titulo': 'Novo hospital é inaugurado em João Pessoa',
            'data': '08/12/2025',
            'fonte': 'Correio da Paraíba'
        },
        {
            'titulo': 'Festival cultural movimenta Campina Grande',
            'data': '05/12/2025',
            'fonte': 'Jornal da Paraíba'
        },
    ]
    return render(request, 'home/noticias.html', {'noticias': noticias_fake})


