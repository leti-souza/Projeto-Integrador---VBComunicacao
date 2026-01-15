from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),       # 👈 login e cadastro
    path('noticias/', include('noticias.urls')),
]
