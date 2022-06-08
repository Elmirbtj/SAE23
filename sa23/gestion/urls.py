from django.urls import path
from . import views

urlpatterns = [
    path('etudiant/', views.etudiant),
    path('home/', views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path("update/<int:id>",views.update),
    path("delete/<int:id>", views.delete),
]
