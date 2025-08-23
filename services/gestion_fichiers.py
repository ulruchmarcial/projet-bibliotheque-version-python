import json
import os
from models.livre import Livre
from models.utilisateur import Utilisateur
from models.emprunt import Emprunt
from models.emprunt import *

def sauvegarde_livres(liste_livres):
    # Crée le dossier 'data' s'il n'existe pas
    os.makedirs("data", exist_ok=True)
    with open("data/livres.json", "w", encoding="utf-8") as fichier:
        json.dump([livre.__dict__ for livre in liste_livres], fichier, indent=4,ensure_ascii=False)

   
def charger_livres():
    
    try:
        with open("data/livres.json", "r", encoding="utf-8") as fichier:
            data = json.load(fichier)
            return [Livre(**d) for d in data]
    except FileNotFoundError:
        return []


def sauvegarde_utilisateurs(liste_utilisateur):
    # Crée le dossier 'data' s'il n'existe pas
    os.makedirs("data", exist_ok=True)
    with open("data/utilisateurs.json", "w", encoding="utf-8") as fichier:
        json.dump([utilisateur.__dict__ for utilisateur in liste_utilisateur], fichier, indent=4,ensure_ascii=False)
   

def charger_utilisateurs():
    try:
        with open("data/utilisateurs.json", "r") as fichier:
            data = json.load(fichier)
            return [Utilisateur(**d) for d in data]
    except FileNotFoundError:
        return []
    


def sauvegarde_emprunt(liste_emprunts):
    # Crée le dossier 'data' s'il n'existe pas
    os.makedirs("data", exist_ok=True)
    with open("data/emprunts.json", "w", encoding="utf-8") as fichier:
        json.dump([
            {
                "id_emprunt": emprunt.id_emprunt,
                "id_utilisateur": emprunt.id_utilisateur,
                "id_livre": emprunt.id_livre,
                "date_emprunt": emprunt.date_emprunt.isoformat(),
                "date_retour": emprunt.date_retour.isoformat()
            }
            for emprunt in liste_emprunts
        ], fichier, indent=4 ,ensure_ascii=False)


# def charger_emprunt():
#     try:
#         with open("data/emprunts.json", "r") as fichier:
#             data = json.load(fichier)
#             return [Emprunt(**d) for d in data]
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

def charger_emprunt():
    try:
        with open("data/emprunts.json", "r") as fichier:
            data = json.load(fichier)
            return [Emprunt(**d) for d in data]
            # return data
    except FileNotFoundError:
        return []

