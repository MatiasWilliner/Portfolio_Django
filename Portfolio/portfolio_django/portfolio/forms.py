from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Educacion, Experiencia_laboral, Habilidad, Proyecto, General


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class NewEducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = ['titulo', 'institucion', 'fecha', 'imagen']

class NewHabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['descripcion', 'nivel']

class NewProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo','institucion','fecha','imagen','direccion']

class NewGeneralForm(forms.ModelForm):    
    class Meta:
        model = General
        fields = ['nombre','curso','pais','imagen_portada','imagen_perfil','info_extra']