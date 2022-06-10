from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EtudiantForm(ModelForm):

    class Meta:
        model = models.Etudiant
        fields = ('nom','prenom','groupe','groupe','photo','email')
        labels = {
            'nom' : _('Nom') ,
            'prenom ': _('prenom '),
            'groupe': _('groupe'),
            'photo': _('photo'),
            'email': _('email'),
        }
class ExamensForm(ModelForm):

    class Meta:
        model = models.Examens
        fields = ('id','coefficient','date','titre','resource')
        labels = {
            'id' : _('id') ,
            'coefficient': _('coefficient'),
            'date': _('date'),
            'titre': _('titre'),
            'resource': _('resource'),
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





class UniteForm(ModelForm):

    class Meta:
        model = models.UE
        fields = ('code','nom','semestre','credit')
        labels = {
            'code' : _('code'),
            'nom': _('nom'),
            'semestre': _('semestre'),
            'credit': _('credit'),
        }


class RessourcesForm(ModelForm):

    class Meta:
        model = models.Ressources
        fields = ('code_ressource','nom','descriptif','coefficient',)
        labels = {
            'code_ressource' : _('code ressource'),
            'nom': _('nom'),
            'descriptif': _('descriptif'),
            'coefficient': _('coefficient'),

        }

class EnseignantForm(ModelForm):

    class Meta:
        model = models.Enseignant
        fields = ('id','nom','prenom',)
        labels = {
            'id' : _('id'),
            'nom': _('nom'),
            'prenom': _('prenom'),
        }
