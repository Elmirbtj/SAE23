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


######################################

class UE(models.Model):
    code = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,"code": self.code,"semestre": self.semestre, "credit": self.credit,}

class Ressources(models.Model):
    code_ressource = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)
    coefficient = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"Code ressource": self.code_ressource,"nom": self.nom,"descriptif": self.descriptif, "coefficient": self.coefficient,}

class Enseignant(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"ID": self.id,"nom": self.nom,"prenom": self.prenom,}

