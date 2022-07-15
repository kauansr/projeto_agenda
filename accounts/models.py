from django.db import models
from contatos.models import Contato
from django import forms # form feito pelo django

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato

        exclude = ()
