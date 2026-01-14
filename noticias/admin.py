from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fonte', 'confiavel', 'criada_em')
    list_filter = ('confiavel', 'fonte')
    search_fields = ('titulo', 'conteudo')
