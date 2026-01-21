from django.urls import path
from .views import (
    alternar_favorito,
    home,
    criar_noticia,
    editar_noticia,
    detalhe_noticia,
    metricas,
    definir_confiabilidade,
    noticias_favoritas
)

urlpatterns = [
    path('home/', home, name='home'),
    path('criar/', criar_noticia, name='criar_noticia'),
    path('editar/<int:id>/', editar_noticia, name='editar_noticia'),
    path('detalhe/<int:id>/', detalhe_noticia, name='detalhe_noticia'),
    path('favoritar/<int:noticia_id>/', alternar_favorito, name='alternar_favorito'),
    path('favoritos/', noticias_favoritas, name='noticias_favoritas'),
    

    # MÉTRICAS
    path('metricas/', metricas, name='metricas'),
    path(
        'metricas/confiabilidade/<int:noticia_id>/<str:status>/',
        definir_confiabilidade,
        name='definir_confiabilidade'
    ),
]
