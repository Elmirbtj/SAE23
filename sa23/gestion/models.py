from django.db import models

class Etudiant(models.Model):

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.CharField(max_length = 100,null=True)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,}
