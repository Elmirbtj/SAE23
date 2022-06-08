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

