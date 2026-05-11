
# import time


# from interface.menus import * 
# from utils.utilitaires import *
# # MenuPrincipal, SousMenuLivre , sous_menu_emprunts , sous_menu_utilisateurs , SousMenuStatistiques , effacer_ecran , quitter_programme , pause
# from models.livre import Livre

# from  models.utilisateur import Utilisateur
# from services.gestion_fichiers import *
# from services.gestion_emprunt import *
# from services.gestion_livre import *
# from services.gestion_utilisateur import *
# from services.gestion_statistiques import *
# from  models.emprunt import Emprunt


# # variables globales

# liste_livres = charger_livres()
# liste_utilisateurs = charger_utilisateurs()
# liste_emprunts = charger_emprunt()
from utils.variables_blogale import *




while True :
    
    MenuPrincipal()
    choix = votre_choix_lettre()
    match choix:
        case "A":
            while True:
                effacer_ecran()
                SousMenuLivre()
                choix_A = votre_choix_nombre()
                match choix_A:
                    case 1:
                        nouveau_livre = Livre( )
                        nouveau_livre.SaisirInfosLivre(liste_livres)
                        AjouterLivreDansListe(nouveau_livre, liste_livres)
                        sauvegarde_livres(liste_livres)
                        pause()
                    case 2:
                        recherche_livre(liste_livres)
                        pause()
                    case 3:
                        afficherlistelivre(liste_livres)
                        pause()   
                    case 4:
                        supprimer_livre(liste_livres)
                        pause()
                    case 5:
                        print("⬅️ Retour au menu principal")
                        time.sleep(2)
                        break # Sort du sous-menu mais PAS du menu principal
                    case _:
                        print("❌ Choix invalide, veuillez réessayer.")
                        pause()
        case "B":
            while True:
                effacer_ecran()
                sous_menu_utilisateurs()
                choix_B = votre_choix_nombre()
                match choix_B:
                    case 1:
                        nouvelutilisateur = Utilisateur()
                        nouvelutilisateur.SaisirInfosUtilisateur(liste_utilisateurs)
                        # nouvelutilisateur = Utilisateur(1 , "ahmed" , "ulruch", "rue du pere ", "hyted@hdbd", 5816885475)
                        # nouvelutilisateur1 = Utilisateur(2 , "NGOMEN" , "MARCIAL", "rue du pere ", "hyted@hdbd", 5816885475)
                        # nouvelutilisateur2 = Utilisateur(3 , "ALEX" , "RICHARD", "rue du pere ", "hyted@hdbd", 5816885475)
                        # AjouterUtilisateurDansListe(nouvelutilisateur, liste_utilisateurs)
                        # AjouterUtilisateurDansListe(nouvelutilisateur1, liste_utilisateurs)
                        # AjouterUtilisateurDansListe(nouvelutilisateur2, liste_utilisateurs)

                        AjouterUtilisateurDansListe(nouvelutilisateur, liste_utilisateurs)
                        sauvegarde_utilisateurs(liste_utilisateurs)
                        pause()
                    case 2:
                        effacer_ecran()
                        AfficherListeUtilisateur(liste_utilisateurs)
                        pause()
                    case 3:
                        effacer_ecran()
                        supprimer_utilisateur(liste_utilisateurs) 
                        pause() 
                    case 4:
                         print("⬅️ Retour au menu principal")
                         time.sleep(1)
                         break # Sort du sous-menu mais PAS du menu principal
                    case _:
                        print("❌ Choix invalide, veuillez réessayer.")
                        time.sleep(1)

        case "C":
            while True:
                effacer_ecran()
                sous_menu_emprunts()
                choix_C = votre_choix_nombre()
                match choix_C:
                    case 1:
                        effacer_ecran()
                        nouvel_emprunt = Emprunt()
                        nouvel_emprunt.saisir_infos_emprunt(liste_utilisateurs , liste_livres)
                        AjouterEmpruntDansListe(nouvel_emprunt , liste_emprunts)
                        sauvegarde_emprunt(liste_emprunts)
                        pause()
                    case 2:
                        effacer_ecran()
                        traiter_retour_emprunt(liste_emprunts , liste_utilisateurs , liste_livres)

                        pause()
                    case 3:
                        effacer_ecran()
                        AfficherListeEmprunts(liste_emprunts)
                        pause()
                    case 4:
                        effacer_ecran()
                        rechercher_emprunt(  liste_emprunts , liste_utilisateurs , liste_livres)
                        pause()
                    case 5:
                         print("⬅️ Retour au menu principal")
                         time.sleep(1)
                         break # Sort du sous-menu mais PAS du menu principal
                    case _:
                        print("❌ Choix invalide, veuillez réessayer.")
                        time.sleep(1)

                    
        case "D":
            while True:
                effacer_ecran()
                SousMenuStatistiques()
                choix_D = votre_choix_nombre()
                match choix_D:
                    case 1:
                        effacer_ecran()
                        nombre_total_livre(liste_livres)
                        pause()
                    case 2:
                        effacer_ecran()
                        nombre_total_utilisateur(liste_utilisateurs)
                        pause()
                    case 3:
                        effacer_ecran()
                        nombre_total_emprunt(liste_emprunts)
                        pause()
                    case 4:
                        print("⬅️ Retour au menu principal")
                        time.sleep(1)
                        break
        case "Q":
            print("Merci d’avoir utilisé la bibliothèque. 👋")
            quitter_programme()
            break
        case _:
            print("❌ Choix invalide, veuillez réessayer.")
            time.sleep(1)


            





    # # nouveau_livre = Livre()
    # nouveau_livre = Livre(1 ,"maths"  , "jean" , 2002 ,"roman", 12  )
    # # nouveau_livre = Livre(2 ,"francais"  , "pierre" , 2004 ,"theatre", 80 )
    # # nouveau_livre.SaisirInfosLivre()
    # bibliotheque.AjouterLivreDansListe(nouveau_livre)
    # bibliotheque.afficherlistelivre()

    # nouvelutilisateur = Utilisateur()
    # nouvelutilisateur = Utilisateur(12 , "ahmed" , "ulruch", "rue du pere ", "hyted@hdbd", 5816885475)
    # nouvelutilisateur.SaisirInfostilisateur()
    # bibliotheque.AjouterUtilisateurDansListe(nouvelutilisateur)
    # bibliotheque.AfficherListeUtilisateur()
