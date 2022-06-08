from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from .forms import EtudiantForm

def etudiant(request):
    return render(request,'gestion/etudiant.html')



def home(request):
    liste = list(models.Etudiant.objects.all())
    return render(request, 'gestion/home.html ', {'liste': liste,})



def ajout(request):
    if request.method == "POST":

        form = EtudiantForm(request)
        if form.is_valid():
            etudiant = form.save()
            return render(request,"/gestion/affiche.html",{"etudiant" : etudiant})

        else:
            return render(request,"gestion/ajout.html",{"form": form})
    else :
        form = EtudiantForm()
        return render(request,"gestion/ajout.html",{"form" : form})


def traitement(request):
    form = EtudiantForm(request.POST, request.FILES)
    if form.is_valid():
        etudiant = form.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/ajout.html",{"form": form})


def affiche(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)

    return render(request,"gestion/affiche.html",{"etudiant": etudiant})



def update(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    eform = EtudiantForm(etudiant.dico())
    return render(request, "gestion/update.html", {"eform": eform,"id":id})



def traitementupdate(request, id):
    eform = EtudiantForm(request.POST, request.FILES)
    if eform.is_valid():
        etudiant = eform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/gestion/ajout")
    else:
        return render(request, "gestion/update.html", {"eform": eform, "id": id})






def delete(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/gestion/home")

