from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/usuarios/login/', permanent=False)),
    
    path('admin/', admin.site.urls),

    # ✅ usuários com prefixo /usuarios/
    path('usuarios/', include('usuarios.urls')),

    # ✅ notícias
    path('noticias/', include('noticias.urls')),

    # logout
    path(
    'logout/',
    LogoutView.as_view(next_page='/usuarios/login/'), name='logout'),
]
