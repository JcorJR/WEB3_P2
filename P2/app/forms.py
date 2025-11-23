from django import forms
from app.models import Contato
#Formulário de usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password']
        labels = {
            'username':'Usuario',
            'email': 'E-mail',
        }
        
class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields= ['mensagem']