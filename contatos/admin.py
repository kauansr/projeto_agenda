from django.contrib import admin
from .models import Categoria, Contato # importa de models do bd

# classe de display
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria','mostrar')

    list_display_links = ('id', 'nome', 'sobrenome')

    #list_filter = ('nome', 'sobrenome')

    list_per_page: 10

    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

# coloca as classes no site
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
