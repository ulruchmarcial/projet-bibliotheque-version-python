from utils.utilitaires import *

from services.gestion_fichiers import *


# fonction pour ajouter un livre dans la  liste des livres

def AjouterLivreDansListe( livre , liste_livres ):
    
    if livre.id_livre == 0 or livre.titre =="":
        print("livre invalide ")
        return
    else:
        liste_livres.append(livre)
    print(f"\n📚 Livre '{livre.titre}' ajouté avec succès !")
    # print(f"ID : {livre.id} | Auteur : {livre.auteur} | Exemplaires : {livre.nombre_exemplaire}")


# fonction pour afficher  la  liste des livres

def afficherlistelivre(liste_livres) :
    print("Liste des livres".center(60, "*"))
    print()
    if not  liste_livres:
        print("la liste des livres est vide ....")
    else:
        for livre in liste_livres:
            if livre.id_livre == 0 or livre.titre =="":
                continue
            print(livre)



# fonction pour rechercher  un livre  dans liste des livres
def recherche_livre(liste_livre):
    id = demande_id()
    if existe_livre_par_id(id , liste_livre):
        for livre in liste_livre:
            if livre.id_livre == id:
                print()
                print( " livre trouvé !!!! \n")
                print(livre)
                print()
    else:
        print()
        print(" Ce livre n'exite pas !")


 # fonction pour supprimer  un livre  de la liste des livres

def supprimer_livre(liste_livre):
    print("vous êtes sur le point de supprimer un Livre...")
    if demande_si_continuer():
        id = demande_id()
        if existe_livre_par_id(id , liste_livre) :
            for livre in liste_livre:
                if livre.id_livre == id :
                    reponse = input(f"Voulez vous vraiment supprimez Ce livre ? Y/N : {livre} ?").strip().upper()[0]
                    if reponse == "Y":
                        liste_livre.remove(livre)
                    else:
                        return
            print("📚 Livre supprimé avec succès !")
            sauvegarde_livres(liste_livre)
        else:
            print("ce livre n'exite pas dans la bibliotheque ")
        