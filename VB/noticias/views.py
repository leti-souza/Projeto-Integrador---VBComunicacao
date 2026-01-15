#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
#from django.db.models import Q
#from django.core.paginator import Paginator
#from .models import Noticia


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Noticia

@login_required
def criar_noticia(request):
    if request.method == 'POST':
        Noticia.objects.create(
            titulo=request.POST['titulo'],
            fonte=request.POST['fonte'],
            link=request.POST['link'],
            conteudo=request.POST['conteudo'],
            confiavel=request.POST.get('confiavel') == 'on'
        )
        return redirect('home')

    return render(request, 'noticias/criar_noticia.html')

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required

@permission_required('noticias.change_noticia')
def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    if request.method == 'POST':
        noticia.titulo = request.POST['titulo']
        noticia.fonte = request.POST['fonte']
        noticia.link = request.POST['link']
        noticia.conteudo = request.POST['conteudo']
        noticia.confiavel = request.POST.get('confiavel') == 'on'
        noticia.save()
        return redirect('home')

    return render(request, 'noticias/editar_noticia.html', {'noticia': noticia})


@login_required
def home(request):
    query = request.GET.get('q', '')
    data = request.GET.get('data', '')
    confiavel = request.GET.get('confiavel', '')

    noticias = Noticia.objects.all().order_by('-criada_em')

    # Filtro por palavra-chave
    if query:
        noticias = noticias.filter(
            Q(titulo__icontains=query) |
            Q(conteudo__icontains=query) |
            Q(fonte__icontains=query)
        )

    # Filtro por data
    if data:
        noticias = noticias.filter(criada_em__date=data)

    # Filtro por confiabilidade
    if confiavel == '1':
        noticias = noticias.filter(confiavel=True)
    elif confiavel == '0':
        noticias = noticias.filter(confiavel=False)

    # Paginação
    paginator = Paginator(noticias, 5)  # 5 notícias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'noticias/home.html', {
        'page_obj': page_obj,
        'query': query,
        'data': data,
        'confiavel': confiavel
    })
