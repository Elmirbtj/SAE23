from django.db import models

class Etudiant(models.Model):

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.CharField(max_length = 100,null=True)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,}





class Examens(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null = True)
    coefficient = models.CharField(max_length=100)

    def __str__(self):
        return  self.titre

    def dico(self):
        return {"id": self.id,"titre": self.titre,"date": self.date, "coefficient": self.coefficient,}


class Examens(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    coefficient = models.CharField(max_length=100)

    def __str__(self):
        return self.titre

    def dico(self):
        return {"id": self.id, "titre": self.titre, "date": self.date, "coefficient": self.coefficient, }




class Notes(models.Model):
    examen = models.CharField(max_length=100)
    etudiant =models.CharField(max_length=100)
    note =models.IntegerField(blank=False, null=True)
    appreciation =models.CharField(max_length=100)

    def __str__(self):
        return self.note


def dico(self):
    return {"examen": self.examen, "note": self.note, "etudiant": self.etudiant, "appreciation": self.appreciationt, }
