from django.db import models
from django.contrib.auth.models import User

class Pagina(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='siteLogo/',null=True, blank=True)
    chamada = models.TextField(max_length=100)
    sobre = models.TextField(max_length=500)
    imagem_sobre = models.ImageField(upload_to='imagemSobre/',null=True, blank=True)
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/',null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)
    
    def total(self):
        return self.quantidade * self.produto.preco
    
class Contato(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)