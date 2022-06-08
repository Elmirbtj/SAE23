from django.db import models

class Etudiant(models.Model):

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.CharField(max_length = 100,null=True)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,}





class Unite(models.Model):
    code = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,"code": self.code,"semestre": self.semestre, "credit": self.credit,}

