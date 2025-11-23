from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Rotas do CRUD Usuário
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.loginUsuario, name='loginUsuario'),
    path('cadastro_usuario', views.cadastroUsuario, name='cadastroUsuario'),
    path('logout', views.logoutUsuario, name='logoutUsuario'),
]