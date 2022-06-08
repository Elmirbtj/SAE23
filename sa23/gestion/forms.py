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



class ExamensForm(ModelForm):

    class Meta:
        model = models.Examens
        fields = ('id','coefficient','date','titre')
        labels = {
            'id' : _('id') ,
            'coefficient': _('coefficient'),
            'date': _('date'),
            'titre': _('titre'),
        }
        localized_fields = ('date',)



class NotesForm(ModelForm):

    class Meta:
        model = models.Notes
        fields = ('examen','etudiant','note','appreciation')
        labels = {
            'examen' : _('examen') ,
            'etudiant': _('etudiant'),
            'note': _('note'),
            'appreciation': _('appreciation'),
        }