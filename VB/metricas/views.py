from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from noticias.models import Noticia

def is_coordenador(user):
    return user.groups.filter(name='Coordenacao').exists()

@login_required
@user_passes_test(is_coordenador)
def painel_metricas(request):
    ranking = Noticia.objects.order_by('-visualizacoes')[:5]

    return render(request, 'metricas/painel.html', {
        'ranking': ranking
    })
