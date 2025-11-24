from django.contrib import admin
from app.models import Produto, Contato, Pagina

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome","descricao","estoque","preco")

class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email_usuario", "mensagem", "criado_em")

    def email_usuario(self, obj):
        return obj.usuario.email
    
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("nome","logo","chamada","sobre","endereco","email")
    
    
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Contato,ContatoAdmin)