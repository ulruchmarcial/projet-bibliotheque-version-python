import json
from livre import Livre
from bibliotheque import *
from utilisateur import Utilisateur
from emprunt import *

def sauvegarde_livres(liste_livres):
    with open("livres.json", "w") as fichier:
        json.dump([livre.__dict__ for livre in liste_livres], fichier, indent=4)

   
def charger_livres():
    
    try:
        with open("livres.json", "r") as fichier:
            data = json.load(fichier)
            return [Livre(**d) for d in data]
    except FileNotFoundError:
        return []


def sauvegarde_utilisateurs(liste_utilisateur):
    with open("utilisateurs.json", "w") as fichier:
        json.dump([utilisateur.__dict__ for utilisateur in liste_utilisateur], fichier, indent=4)

def charger_utilisateurs():
    try:
        with open("utilisateurs.json", "r") as fichier:
            data = json.load(fichier)
            return [Utilisateur(**d) for d in data]
    except FileNotFoundError:
        return []
    


# def sauvegarde_emprunt(liste_emprunts):
#     with open("emprunts.json", "w") as fichier:
#         json.dump([
#             {
#                 "id_emprunt": emprunt.id_emprunt,
#                 "id_utilisateur": emprunt.id_utilisateur,
#                 "id_livre": emprunt.id_livre,
#                 "date_emprunt": emprunt.date_emprunt.isoformat(),
#                 "date_retour": emprunt.date_retour.isoformat()
#             }
#             for emprunt in liste_emprunts
#         ], fichier, indent=4)


# def charger_emprunt(bibliotheque= None):
#     try:
#         with open("emprunts.json", "r") as fichier:
#             data = json.load(fichier)
#             return [Emprunt(bibliotheque=bibliotheque,**d) for d in data]
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def charger_emprunt():
#     try:
#         with open("emprunts.json", "r") as fichier:
#             data = json.load(fichier)
#             # return [Emprunt(**d) for d in data]
#             return data
#     except FileNotFoundError:
#         return []