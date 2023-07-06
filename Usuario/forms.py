from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion

class PostForm(forms.ModelForm):
    content = forms.ImageField(label='')

    class Meta:
        model = Publicacion
        fields = ['content']