from django.urls import path
from .views import login_view, cadastro_view

urlpatterns = [
    path('', cadastro_view, name='cadastro'),
    path('login/', login_view, name='login'),
]
