from django.urls import path
from .views import painel_metricas

urlpatterns = [
    path('', painel_metricas, name='painel_metricas'),
]
