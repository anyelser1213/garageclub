from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.inventario_stock.models import *
from aplicaciones.usuarios.models import Usuarios



###################### AQUI COMIENZAN LOS FORMULARIOS PARA TODO DE INVENTARIO ##########################################
'''
class CalidadForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(CalidadForm, self).__init__(*args, **kwargs)
        print("Formulario CalidadForm: \n")
        #print("usuario: ",self.usuarioID)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Calidad
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }


'''

class NewUserForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = '__all__'


class UsuarioPersonalizadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(UsuarioPersonalizadoForm, self).__init__(*args, **kwargs)
        print("Formulario UsuarioPersonalizado: \n")
        print("usuario: ",usuario_id)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Usuarios
        #fields = "__all__"

        #Estos campos no son necesarios en el registro normal de usuarios
        exclude = ('user_permissions','groups','last_login','activo','admin','is_superuser','imagenPerfil','password','tabla_Discipulos','usuarios_roles')
        widgets = {
            #"nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }
