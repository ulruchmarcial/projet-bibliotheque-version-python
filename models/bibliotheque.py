from fichiers import *
from utilitaires import *
from emprunt import Emprunt
from livre import Livre


class Bibliotheque:
    livre = Livre()
    def __init__(self):
        self.liste_livres = []
        self.liste_utilisateurs = []
        self.liste_emprunts =[]
        


# # fonction pour ajouter un livre dans la  liste des livres

#     def AjouterLivreDansListe(self, livre ):
#         if livre.id_livre == 0 or livre.titre =="":
#             print("livre invalide ")
#             return
#         else:
#             self.liste_livres.append(livre)
#         print(f"\n📚 Livre '{livre.titre}' ajouté avec succès !")
#         # print(f"ID : {livre.id} | Auteur : {livre.auteur} | Exemplaires : {livre.nombre_exemplaire}")

# # fonction pour afficher  la  liste des livres

#     def afficherlistelivre(self) :
#         print("Liste des livres".center(60, "*"))
#         print()
#         if not  self.liste_livres:
#             print("la liste des livres est vide ....")
#         else:
#             for livre in self.liste_livres:
#                 if livre.id == 0 or livre.titre =="":
#                     continue
#                 print(livre)

# # fonction pour ajouter un utilisateur  dans la  liste des utilisateur

#     def AjouterUtilisateurDansListe(self , utilisateur):
#         self.liste_utilisateurs.append(utilisateur)
#         print(f"\n📚 Utilisateur '{utilisateur.nom}' ajouté avec succès !")

# fonction pour afficher  la  utilisateur
    # def AfficherListeUtilisateur(self):
    #     print("Liste Des Utilisateurs".center(60, "+"))
    #     print()
    #     if not self.liste_utilisateurs:
    #         print("la liste des utilisateur est vide ")
    #         return
    #     for utilisateur in self.liste_utilisateurs:
    #         print(utilisateur)

# # fonction pour ajouter un emprunt  dans la  liste des emprunts

#     def AjouterEmpruntDansListe(self , emprunt):
#         self.liste_emprunts.append(emprunt)
#         print(f"\n📚 Le livre a ete  emprunté !")
#         print()

# # fonction pour afficher  la liste des emprunts

#     def AfficherListeEmprunts(self):
#         print("Liste Des Emprunts".center(60, "+"))
#         print()
#         if not self.liste_emprunts:
#             print("la liste des emprunts est vide ")
#             return
#         for emprunt in self.liste_emprunts:
#             print(emprunt)
     
    # # fonction pour demander in identifiant afin d'executer une action 
    # def demande_id(self):
    #      while True:
    #         try:
    #             id = int(input ("Entrer  son identifiant  (entre 0 et 100) :  "))
    #             if id < 1 or id > 100:
    #                 print(" vous devez entrer un identifiant compris entre 0 et 100. réessayez ")
    #             else:
    #                 return id
    #         except ValueError:
    #                 print(" vous devez entrer un identifiant valide réessayez. ")
            
         

 # fonction pour rechercher  un livre  dans liste des livres
    # def recherche_livre(self):
        
    #     id = self.demande_id()
    #     if existe_livre_par_id(id , self.liste_livres):
    #         for livre in self.liste_livres:
    #             if livre.id == id:
    #                 print()
    #                 print( " livre trouvé !!!! \n")
    #                 print(livre)
    #                 print()
    #     else:
    #         print()
    #         print(" Ce livre n'exite pas !")
    
    # fonction pour supprimer  un livre  de la liste des livres

    # def supprimer_livre(self):
    #     print("vous êtes sur le point de supprimer un Livre...")
    #     if demande_si_continuer():
    #         id = self.demande_id()
    #         if existe_livre_par_id(id , self.liste_livres) :
    #             for livre in self.liste_livres:
    #                 if livre.id == id :
    #                     reponse = input(f"Voulez vous vraiment supprimez Ce livre ? Y/N : {livre} ?").strip().upper()[0]
    #                     if reponse == "Y":
    #                         self.liste_livres.remove(livre)
    #                     else:
    #                         return
    #             print("📚 Livre supprimé avec succès !")
    #         #sauvegarde_livres(self.liste_livres)
    #         else:
    #             print("ce livre n'exite pas dans la bibliotheque ")
    #         sauvegarde_livres(self.liste_livres)
        
#  # fonction pour retourner un livre
#     def traiter_retour_emprunt(self):
#         while True:
#             try:
#                 mode = int(input('''Veuillez choisir votre mode de recherche : 
#     1. Rechercher par ID de l'emprunt 
#     2. Rechercher par ID utilisateur et ID livre
#     > '''))
#                 if mode not in [1, 2]:
#                     print("⚠️ Vous devez choisir 1 ou 2.")
#                     continue
#             except ValueError:
#                 print("⚠️ Vous devez entrer uniquement 1 ou 2.")
#                 continue

#             if mode == 1:
#                 emprunt = self.recherche_emprunt_par_id_emprunt()
#             else:
#                 emprunt = self.recherche_emprunt_par_id_utilisateur()

#             # Traitement du retour
#             if emprunt:
#                 livre_trouve = False
#                 for livre in self.liste_livres:
#                     if livre.id == emprunt.id_livre:
#                         livre.nombre_exemplaire += 1
#                         livre_trouve = True
#                         break

#                 if not livre_trouve:
#                     print("⚠️ Le livre emprunté n'est plus dans le catalogue. Veuillez le réenregistrer.")
#                     nouveau_livre = Livre()  
#                     nouveau_livre.SaisirInfosLivre()  
#                     self.liste_livres.append(nouveau_livre)
#                     #sauvegarde_livres(self.liste_livres)
#             else:
#                 print("❌ Aucun emprunt trouvé.")
#             sauvegarde_livres(self.liste_livres)
#             break  # Fin de boucle après un traitement

       
    # fonction pour supprimer  un Utilisateur  de la liste des Utilisateurs    

    # def supprimer_utilisateur(self):
    #     print("vous êtes sur le point de supprimer un Utilisateur...")
    #     if demande_si_continuer():
    #         id = self.demande_id()
    #         if existe_utilisateur_par_id(id , self.liste_utilisateurs ):
    #             for utilisateur in self.liste_utilisateurs:
    #                 if utilisateur.id == id :
    #                     reponse = input(f"Voulez vous vraiment supprimez cet-utilisateur ? Y/N : {utilisateur} ?").strip().upper()[0]
    #                     if reponse == "Y":
    #                         self.liste_utilisateurs.remove(utilisateur)
    #                         print("📚 Utilisateur supprimé avec succès !")
    #                         sauvegarde_utilisateurs(self.liste_utilisateurs)
    #                     else :
    #                         return  
                                    
    #         else:
    #             print(f" Cet utilisateur n'exite pas dans la bibliotheque ")

    # # fonction pour verifier qu'un Emprunt exite dans  liste des Emprunts
    # def exite_emprunt(self, emprunt):
    #     for emprunt in self.liste_emprunts:
    #         if emprunt  == emprunt :
    #             return True
    #         else:
    #             return False
 
    # # fonction pour rechercher  un Emprunt dans  liste des Emprunts
    # def recherche_emprunt_par_id_emprunt(self):
    #     id = input("Entrer l'identifiant de l'emprunt : ").strip().upper()
    #     for emprunt in self.liste_emprunts:
           
    #             if emprunt.id_emprunt == id:
    #                 print (" Emprunt trouvé !!!!")
    #                 return emprunt
    #             else:
    #                 print(f"Aucun emprunt trouvé avec l'identifiant : {id}")
    #                 return 
  

    # def recherche_emprunt_par_id_utilisateur(self):
    #     print(" Entrer l'identifiant de l'utilisateur ")
    #     id_utilisateur = self.demande_id()
    #     if existe_utilisateur_par_id(id_utilisateur  , self.liste_utilisateurs):
    #         print(" Entrer l'identifiant du livre ")
    #         id_livre = self.demande_id()
    #         if existe_livre_par_id(id_livre , self.liste_livres):
    #             for emprunt in self.liste_emprunts:
                   
    #                     if emprunt.id_utilisateur == id_utilisateur and emprunt.id_livre == id_livre:
    #                         print("Emprunt trouvé ")
    #                         return emprunt
    #                     else:
    #                         print("Aucun emprunt trouvé !!!!!")
                    

    #         else:
    #             print(f"Aucun livre trouvé avec l'identifiant : {id_livre}")
    #     else:
    #             print(f"Aucun utlisateur trouvé avec l'identifiant : {id_utilisateur}")
                    
    


        



        
