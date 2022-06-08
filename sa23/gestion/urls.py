from django.urls import path
from . import views
from django.contrib import admin
from .views import *

urlpatterns = [
    path('etudiant/', views.etudiant),
    path('home/', views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path("update/<int:id>",views.update),
    path("delete/<int:id>", views.delete),


    path('examens/', views.examens),
    path('ajout_exa/', views.ajout_exa),
    path('traitement_exa/', views.traitement_exa),
    path('affiche_exa/<int:id>/', views.affiche_exa),
    path('traitementupdate_exa/<int:id>/', views.traitementupdate_exa),
    path("update_exa/<int:id>", views.update_exa),
    path("delete_exa/<int:id>", views.delete_exa),


    path('note/', views.note),
    path('ajout_note/', views.ajout_note),
    path('traitement_note/', views.traitement_note),
    path('affiche_note/<int:id>/', views.affiche_note),
    path('traitementupdate_note/<int:id>/', views.traitementupdate_note),
    path("update_note/<int:id>", views.update_note),
    path("delete_note/<int:id>", views.delete_note),



]
