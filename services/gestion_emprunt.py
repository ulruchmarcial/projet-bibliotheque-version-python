from utils.utilitaires import *
from models.livre import Livre
from services.gestion_fichiers import *
# fonction pour ajouter un emprunt  dans la  liste des emprunts

def AjouterEmpruntDansListe( emprunt , liste_emprunts ):
    if emprunt.id_emprunt == 0 or emprunt.id_livre == 0 :
        print("impossible d'enregistrer un emprunt avec des identifiants null\n")
        return
    liste_emprunts.append(emprunt)
    print(f"\n📚 Le livre a ete  emprunté !")
    print()

# fonction pour afficher  la liste des emprunts

def AfficherListeEmprunts(liste_emprunts):
    print("Liste Des Emprunts".center(60, "+"))
    print()
    if not liste_emprunts:
        print("la liste des emprunts est vide ")
        return
    for emprunt in liste_emprunts:
        print(emprunt)


 # fonction pour rechercher  un Emprunt dans  liste des Emprunts

def recherche_emprunt_par_id_emprunt( liste_emprunts):
    id = input("Entrer l'identifiant de l'emprunt : ").strip().upper()
    for emprunt in liste_emprunts:
        
            if emprunt.id_emprunt == id:
                print (" Emprunt trouvé !!!!")
                return emprunt
            
    print(f"Aucun emprunt trouvé avec l'identifiant : {id}")
    return None

def recherche_emprunt_par_id_utilisateur(liste_emprunts , liste_utilisateurs , liste_livres):
    print(" Entrer l'identifiant de l'utilisateur ")
    id_utilisateur = demande_id()
    if existe_utilisateur_par_id(id_utilisateur  , liste_utilisateurs):
        print(" Entrer l'identifiant du livre ")
        id_livre = demande_id()
        if existe_livre_par_id(id_livre , liste_livres):
            for emprunt in liste_emprunts:
                
                    if emprunt.id_utilisateur == id_utilisateur and emprunt.id_livre == id_livre:
                        print("Emprunt trouvé ")
                        return emprunt
                    # else:
            print("Aucun emprunt trouvé !!!!!")
            return None
                

        else:
            print(f"Aucun livre trouvé avec l'identifiant : {id_livre}")
    else:
            print(f"Aucun utlisateur trouvé avec l'identifiant : {id_utilisateur}")

    
# fonction pour verifier qu'un Emprunt exite dans  liste des Emprunts

def exite_emprunt( emprunt , liste_emprunts):
    for emprunt in liste_emprunts:
        if emprunt  == emprunt :
            return True
        else:
            return False
        
#  fonction pour rechercher et afficher un emprunt 
def rechercher_emprunt(  liste_emprunts , liste_utilisateurs , liste_livres):
    while True:
        try:
            mode = int(input('''Veuillez choisir votre mode de recherche : 
1. Rechercher par ID de l'emprunt 
2. Rechercher par ID utilisateur et ID livre
> '''))
            if mode not in [1, 2]:
                print("⚠️ Vous devez choisir 1 ou 2.")
                continue
        except ValueError:
            print("⚠️ Vous devez entrer uniquement 1 ou 2.")
            continue

        if mode == 1:
            emprunt = recherche_emprunt_par_id_emprunt(liste_emprunts)
            print(emprunt)
            break
        else:
            emprunt = recherche_emprunt_par_id_utilisateur(liste_emprunts , liste_utilisateurs , liste_livres)
            print(emprunt)
            break
    
        
    # fonction pour retourner un livre

def traiter_retour_emprunt(liste_emprunts , liste_utilisateurs , liste_livres):
    while True:
        try:
            mode = int(input('''Veuillez choisir votre mode de recherche : 
1. Rechercher par ID de l'emprunt 
2. Rechercher par ID utilisateur et ID livre
> '''))
            if mode not in [1, 2]:
                print("⚠️ Vous devez choisir 1 ou 2.")
                continue
        except ValueError:
            print("⚠️ Vous devez entrer uniquement 1 ou 2.")
            continue

        if mode == 1:
            emprunt = recherche_emprunt_par_id_emprunt(liste_emprunts)
        else:
            emprunt = recherche_emprunt_par_id_utilisateur(liste_emprunts , liste_utilisateurs , liste_livres)

        # Traitement du retour
        if emprunt:
            livre_trouve = False
            for livre in liste_livres:
                if livre.id_livre == emprunt.id_livre:
                    livre.nombre_exemplaire += 1
                    livre_trouve = True
                    # supprimer l'emprunt de la liste d'emprunt
                    liste_emprunts.remove(emprunt)
                    sauvegarde_emprunt(liste_emprunts)
                    break

            if not livre_trouve:
                print("⚠️ Le livre emprunté n'est plus dans le catalogue. Veuillez le réenregistrer.")
                nouveau_livre = Livre()  
                nouveau_livre.SaisirInfosLivre()  
                liste_livres.append(nouveau_livre)
                sauvegarde_livres(liste_livres)
        else:
            print("❌ Aucun emprunt trouvé.")
        sauvegarde_livres(liste_livres)
        break  # Fin de boucle après un traitement