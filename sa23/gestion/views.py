from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from .forms import EtudiantForm
from .forms import ExamensForm
from .forms import NotesForm

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





def examens(request):
    liste1 = list(models.Examens.objects.all())
    return render(request, 'gestion/examens.html ', {'liste1': liste1,})

def ajout_exa(request):
    if request.method == "POST":

        form = ExamensForm(request)
        if form.is_valid():
            examens = form.save()
            return render(request,"/gestion/affiche_exa.html",{"examens" : examens})

        else:
            return render(request,"gestion/ajout_exa.html",{"form": form})
    else :
        form = ExamensForm()
        return render(request,"gestion/ajout_exa.html",{"form" : form})

def traitement_exa(request):
    form = ExamensForm(request.POST, request.FILES)
    if form.is_valid():
        examens = form.save()
        return HttpResponseRedirect("/gestion/examens")
    else:
        return render(request,"gestion/ajout_exa.html",{"form": form})

def affiche_exa(request, id):
    examens = models.Examens.objects.get(pk=id)

    return render(request,"gestion/affiche_exa.html",{"examens": examens})

def update_exa(request, id):
    examens = models.Examens.objects.get(pk=id)
    exform = ExamensForm(examens.dico())
    return render(request, "gestion/update_exa.html", {"exform": exform,"id":id})

def traitementupdate_exa(request, id):
    exform = ExamensForm(request.POST, request.FILES)
    if exform.is_valid():
        examens = exform.save(commit=False)
        examens.id = id
        examens.save()
        return HttpResponseRedirect("/gestion/examens")
    else:
        return render(request, "gestion/update_exa.html", {"exform": exform, "id": id})


def delete_exa(request, id):
    examens = models.Examens.objects.get(pk=id)
    examens.delete()
    return HttpResponseRedirect("/gestion/examens")





def note(request):
    liste_note = list(models.Notes.objects.all())
    return render(request, 'note/note.html ', {'liste_note': liste_note})

def ajout_note(request):
    if request.method == "POST":

        form = NotesForm(request)
        if form.is_valid():
            note = form.save()
            return render(request,"/note/affiche_note.html",{"note" : note})

        else:
            return render(request,"note/ajout_note.html",{"form": form})
    else :
        form = NotesForm()
        return render(request,"note/ajout_note.html",{"form" : form})

def traitement_note(request):
    form = NotesForm(request.POST, request.FILES)
    if form.is_valid():
        note = form.save()
        return HttpResponseRedirect("/gestion/note")
    else:
        return render(request,"note/ajout_note.html",{"form": form})

def affiche_note(request, id):
    note = models.Notes.objects.get(pk=id)

    return render(request,"note/affiche_note.html",{"note": note})

def update_note(request, id):
    note = models.Notes.objects.get(pk=id)
    nform = NotesForm(note.dico())
    return render(request, "note/update_note.html", {"nform": nform,"id":id})

def traitementupdate_note(request, id):
    nform = NotesForm(request.POST, request.FILES)
    if nform.is_valid():
        note = nform.save(commit=False)
        note.id = id
        note.save()
        return HttpResponseRedirect("/note/ajout_note")
    else:
        return render(request, "note/update_note.html", {"nform": nform, "id": id})


def delete_note(request, id):
    note = models.Notes.objects.get(pk=id)
    note.delete()
    return HttpResponseRedirect("/gestion/note")


