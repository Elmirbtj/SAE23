from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EtudiantForm(ModelForm):

    class Meta:
        model = models.Etudiant
        fields = ('nom',)
        labels = {
            'nom' : _('Nom') ,

        }



class UniteForm(ModelForm):

    class Meta:
        model = models.Etudiant
        fields = ('code','nom','semestre','credit')
        labels = {
            'code' : _('code') ,
            'semestre': _('semestre'),
            'credit': _('credit'),
            'nom': _('Nom'),
        }
