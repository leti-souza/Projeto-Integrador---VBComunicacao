from django.urls import path
from .views import editar_noticia, home, criar_noticia

urlpatterns = [
    path('home/', home, name='home'),
    path('criar/', criar_noticia, name='criar_noticia'),
    path('editar/<int:id>/', editar_noticia, name='editar_noticia'),
    
]
