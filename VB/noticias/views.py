from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden

from .models import Noticia, Favorito
from usuarios.models import Perfil  # ✅ pegar tipo do usuário (jornalista/coordenador)


# =========================
# CONTROLE DE PERFIL
# =========================
def is_coordenador(user):
    return user.groups.filter(name='Coordenacao').exists()

def is_jornalista(user):
    return user.groups.filter(name='Jornalista').exists()


# =========================
# MÉTRICAS (COORDENADOR)
# =========================
@login_required
@user_passes_test(is_coordenador)
def metricas(request):
    ranking = Noticia.objects.order_by('-visualizacoes')[:5]
    pauta = Noticia.objects.filter(confiavel__isnull=True)

    favoritas = (
        Noticia.objects
        .annotate(total_favoritos=Count('favoritos'))
        .filter(total_favoritos__gt=0)
        .order_by('-total_favoritos')
    )

    favoritos_detalhe = (
        Favorito.objects
        .select_related('noticia', 'usuario')
        .order_by('-criado_em')
    )

    return render(request, 'noticias/metricas.html', {
        'ranking': ranking,
        'pauta': pauta,
        'favoritas': favoritas,
        'favoritos_detalhe': favoritos_detalhe,
    })


@login_required
@user_passes_test(is_coordenador)
def definir_confiabilidade(request, noticia_id, status):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if status == 'confiavel':
        noticia.confiavel = True
    elif status == 'nao_confiavel':
        noticia.confiavel = False

    noticia.save()
    return redirect('metricas')


# =========================
# NOTÍCIAS
# =========================
@login_required
def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.visualizacoes += 1
    noticia.save()
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})


@login_required
def criar_noticia(request):
    if request.method == 'POST':
        Noticia.objects.create(
            titulo=request.POST['titulo'],
            fonte=request.POST['fonte'],
            link=request.POST['link'],
            conteudo=request.POST['conteudo'],
            confiavel=None
        )
        return redirect('home')

    return render(request, 'noticias/criar_noticia.html')


@login_required
def editar_noticia(request, id):
    if not is_coordenador(request.user):
        return HttpResponseForbidden('Acesso negado')

    noticia = get_object_or_404(Noticia, id=id)

    if request.method == 'POST':
        noticia.titulo = request.POST['titulo']
        noticia.fonte = request.POST['fonte']
        noticia.link = request.POST['link']
        noticia.conteudo = request.POST['conteudo']

        noticia.confiavel = 'confiavel' in request.POST
        noticia.save()
        return redirect('home')

    return render(request, 'noticias/editar_noticia.html', {'noticia': noticia})


# =========================
# HOME
# =========================
@login_required
def home(request):
    query = request.GET.get('q', '')
    data = request.GET.get('data', '')
    confiavel = request.GET.get('confiavel', '')

    noticias = Noticia.objects.all().order_by('-criada_em')

    if query:
        noticias = noticias.filter(
            Q(titulo__icontains=query) |
            Q(conteudo__icontains=query) |
            Q(fonte__icontains=query)
        )

    if data:
        noticias = noticias.filter(criada_em__date=data)

    if confiavel == '1':
        noticias = noticias.filter(confiavel=True)
    elif confiavel == '0':
        noticias = noticias.filter(confiavel=False)

    paginator = Paginator(noticias, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # FLAGS PARA TEMPLATE
    is_coordenador_flag = is_coordenador(request.user)
    is_jornalista_flag = is_jornalista(request.user)

    favoritos_ids = set()
    if is_jornalista_flag:
        favoritos_ids = set(
            Favorito.objects.filter(usuario=request.user)
            .values_list('noticia_id', flat=True)
        )

    # ✅ tipo do usuário vindo do Perfil (usuarios.Perfil.tipo)
    perfil = Perfil.objects.filter(user=request.user).first()
    tipo_usuario = ''
    if perfil and perfil.tipo:
        # deixa bonitinho: "coordenador" -> "Coordenador"
        tipo_usuario = perfil.tipo.replace('_', ' ').title()

    # opcional: mostrar email na navbar (se tiver)
    email_usuario = request.user.email or request.user.username

    return render(request, 'noticias/home.html', {
        'page_obj': page_obj,
        'query': query,
        'data': data,
        'confiavel': confiavel,
        'is_coordenador': is_coordenador_flag,
        'is_jornalista': is_jornalista_flag,
        'favoritos_ids': favoritos_ids,

        # ✅ novos
        'tipo_usuario': tipo_usuario,
        'email_usuario': email_usuario,
    })


# =========================
# FAVORITOS (JORNALISTA)
# =========================
@login_required
@user_passes_test(is_jornalista)
def alternar_favorito(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    favorito, created = Favorito.objects.get_or_create(
        usuario=request.user,
        noticia=noticia
    )

    if not created:
        favorito.delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
@user_passes_test(is_jornalista)
def noticias_favoritas(request):
    favoritos = (
        Favorito.objects
        .filter(usuario=request.user)
        .select_related('noticia')
        .order_by('-criado_em')
    )

    return render(request, 'noticias/favoritos.html', {
        'favoritos': favoritos
    })
