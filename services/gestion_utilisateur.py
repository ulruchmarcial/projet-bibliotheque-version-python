from utils.utilitaires import *
from services.gestion_fichiers import *


# fonction pour ajouter un utilisateur  dans la  liste des utilisateur

def AjouterUtilisateurDansListe( utilisateur , liste_utilisateur):
    if utilisateur.id_utilisateur == 0 or utilisateur.nom =="":
        print("utilisateur  invalide ")
    else:
        liste_utilisateur.append(utilisateur)
        print(f"\n📚 Utilisateur '{utilisateur.nom}' ajouté avec succès !")

# fonction pour afficher  la  utilisateur

def AfficherListeUtilisateur( liste_utilisateur):
    print("Liste Des Utilisateurs".center(60, "+"))
    print()
    if not liste_utilisateur:
        print("la liste des utilisateur est vide ")
        return
    for utilisateur in liste_utilisateur:
        print(utilisateur)

# fonction pour supprimer  un Utilisateur  de la liste des Utilisateurs  
 
def supprimer_utilisateur(liste_utilisateur):
    print("vous êtes sur le point de supprimer un Utilisateur...")
    if demande_si_continuer():
        id = demande_id()
        if existe_utilisateur_par_id(id , liste_utilisateur ):
            for utilisateur in liste_utilisateur:
                if utilisateur.id_utilisateur == id :
                    reponse = input(f"Voulez vous vraiment supprimez cet-utilisateur ? Y/N : {utilisateur} ?").strip().upper()[0]
                    if reponse == "Y":
                        liste_utilisateur.remove(utilisateur)
                        print("📚 Utilisateur supprimé avec succès !")
                        sauvegarde_utilisateurs(liste_utilisateur)
                    else :
                        return  
                                
        else:
            print(f" Cet utilisateur n'exite pas dans la bibliotheque ")