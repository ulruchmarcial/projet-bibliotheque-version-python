
import time

from menus import * 
from utilitaires import *
# MenuPrincipal, SousMenuLivre , sous_menu_emprunts , sous_menu_utilisateurs , SousMenuStatistiques , effacer_ecran , quitter_programme , pause
from livre import Livre
from bibliotheque import Bibliotheque
from utilisateur import Utilisateur
from fichiers import *
from emprunt import Emprunt


#variables globales
bibliotheque = Bibliotheque()


liste_livres = charger_livres()
bibliotheque.liste_livres = liste_livres

liste_utilisateurs = charger_utilisateurs()
bibliotheque.liste_utilisateurs = liste_utilisateurs

# liste_emprunts = charger_emprunt(bibliotheque )
# bibliotheque.liste_emprunts = liste_emprunts



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
                        nouveau_livre = Livre()
                        nouveau_livre.SaisirInfosLivre()
                        bibliotheque.AjouterLivreDansListe(nouveau_livre)
                        sauvegarde_livres(bibliotheque.liste_livres)
                    case 2:
                        bibliotheque.recherche_livre()
                        pause()
                    case 3:
                        bibliotheque.afficherlistelivre()
                        pause()   
                    case 4:
                        bibliotheque.supprimer_livre()
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
                        nouvelutilisateur.SaisirInfosUtilisateur()
                        bibliotheque.AjouterUtilisateurDansListe(nouvelutilisateur)
                        #sauvegarde_utilisateurs(bibliotheque.liste_utilisateurs)
                    case 2:
                        effacer_ecran()
                        bibliotheque.AfficherListeUtilisateur()
                        pause()
                    case 3:
                        effacer_ecran()
                        bibliotheque.supprimer_utilisateur() 
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
                        nouvel_emprunt = Emprunt(bibliotheque)
                        nouvel_emprunt.saisir_infos_emprunt()
                        bibliotheque.AjouterEmpruntDansListe(nouvel_emprunt)
                        #sauvegarde_emprunt(bibliotheque.liste_emprunts)
                        pause()
                    case 2:
                        effacer_ecran()
                        bibliotheque.traiter_retour_emprunt()

                        pause()
                    case 3:
                        effacer_ecran()
                        bibliotheque.AfficherListeEmprunts()
                        pause()
                    case 4:
                         print("⬅️ Retour au menu principal")
                         time.sleep(1)
                         break # Sort du sous-menu mais PAS du menu principal
                    case _:
                        print("❌ Choix invalide, veuillez réessayer.")
                        time.sleep(1)

                    
        case "D":
            SousMenuStatistiques()
        case "Q":
            print("Merci d’avoir utilisé la bibliothèque. 👋")
            quitter_programme()
            break
        case _:
            print("❌ Choix invalide, veuillez réessayer.")
            break


            





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
