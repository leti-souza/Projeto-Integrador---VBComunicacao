from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Noticia

@login_required
def home(request):
    noticias = Noticia.objects.all().order_by('-criada_em')
    return render(request, 'noticias/home.html', {'noticias': noticias})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from .models import Noticia

@login_required
def home(request):
    query = request.GET.get('q', '')

    noticias = Noticia.objects.all().order_by('-criada_em')

    if query:
        noticias = noticias.filter(
            Q(titulo__icontains=query) |
            Q(conteudo__icontains=query) |
            Q(fonte__icontains=query)
        )

    return render(request, 'noticias/home.html', {
        'noticias': noticias,
        'query': query
    })
