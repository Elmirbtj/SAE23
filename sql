SELECT 
FROM UE INNER JOIN ((Examens INNER JOIN (Etudiant INNER JOIN Notes ON Etudiant.N° = Notes.etudiant) ON Examens.N° = Notes.examens) INNER JOIN (Enseignant INNER JOIN Ressources ON Enseignant.N° = Ressources.[code ressource]) ON Examens.ressources = Ressources.[code ressource]) ON (Notes.N° = UE.N°) AND (UE.N° = Ressources.competence);
