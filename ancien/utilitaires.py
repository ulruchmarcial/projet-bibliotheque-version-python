import os
import time
import msvcrt
import random
import string


# fonction pour effacer l'ecran 
def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

# fonction pour faire une pause 
def pause():
    print("Appuyez sur une touche pour continuer...")
    msvcrt.getch()
    effacer_ecran()

# Fonction pour quitter le programme 
def quitter_programme():
    print("Fermeture du programme dans 5 secondes" , end="" , flush=True )
    for i in range(5):
        time.sleep(1)
        print("." , end="" , flush=True)
    effacer_ecran()


# fonction pour demander si continuer afin d'executer une action 
def demande_si_continuer():
    while True:
        reponse = input("Voulez-vous continuer ? Y/N ").strip().upper()
        if reponse.startswith("Y"):
            return True
        elif reponse.startswith("N"):
            return False
        else:
            print("Veuillez répondre par Y (oui) ou N (non).")

 # fonction pour verifier si un utilisateur exite dans la liste des utilisateurs

def existe_utilisateur_par_id(id_utilisateur , liste_utilisateurs ):
        for utilisateur in liste_utilisateurs:
            if utilisateur.id == id_utilisateur:
                return True
        return False

 # fonction pour verifier si un livre exite dans la liste des livres
def existe_livre_par_id( id_livre , liste_livres):
        for livre in liste_livres:
            if livre.id == id_livre:
                return True
        return False
# fonction pour verifier si un livre exite dans la liste des livres
def generer_id_emprunt(longueur=4):
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=longueur))

# fonction pour demander a l'utilisateur de faire son choix 
def votre_choix_lettre():
    while True:
        saisie = input("Faites votre choix: ").strip().upper()
        if saisie:
            return saisie[0]  # Retourne uniquement la première lettre
        else:
            print("❌ Vous devez entrer au moins une lettre.")

def votre_choix_nombre():
    while True:
        try:
            saisie = int(input("Faites votre choix (1 à 5) : "))
            if saisie in range(1, 6):
                return saisie
            else:
                print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        except ValueError:
            print("❌ Vous devez saisir uniquement un nombre.")


