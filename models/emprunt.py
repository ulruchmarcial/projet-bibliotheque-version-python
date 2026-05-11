
from utils.utilitaires import *

from datetime import date, timedelta , datetime

# class Emprunt:
#     def __init__(self, id_emprunt=0, id_utilisateur=0, id_livre=0,
#                  date_emprunt=None, date_retour=None, bibliotheque=None):
#         self.id_emprunt = id_emprunt or generer_id_emprunt()
#         self.id_utilisateur = id_utilisateur
#         self.id_livre = id_livre
#         self.date_emprunt = date_emprunt if isinstance(date_emprunt, date) else date.fromisoformat(date_emprunt) if date_emprunt else date.today()
#         self.date_retour = date_retour if isinstance(date_retour, date) else date.fromisoformat(date_retour) if date_retour else self.date_emprunt + timedelta(days=14)
#         self.bibliotheque = bibliotheque


class Emprunt:

    def __init__(self, id_emprunt = 0, id_utilisateur = 0, id_livre = 0, date_emprunt =None, date_retour =None ):
        self.id_emprunt = id_emprunt or generer_id_emprunt()
        self.id_utilisateur = id_utilisateur
        self.id_livre = id_livre

        if date_emprunt is None:
            self.date_emprunt = date.today()
        elif isinstance(date_emprunt, str):
            # Convertir la chaîne en objet date
            try:
                self.date_emprunt = datetime.strptime(date_emprunt, '%Y-%m-%d').date()
            except ValueError:
                try:
                    self.date_emprunt = datetime.strptime(date_emprunt, '%d/%m/%Y').date()
                except ValueError:
                    print(f"Format de date invalide: {date_emprunt}")
                    self.date_emprunt = date.today()
        else:
            self.date_emprunt = date_emprunt
            
        # Même logique pour date_retour
        if date_retour is None:
            self.date_retour = None
        elif isinstance(date_retour, str):
            try:
                self.date_retour = datetime.strptime(date_retour, '%Y-%m-%d').date()
            except ValueError:
                try:
                    self.date_retour = datetime.strptime(date_retour, '%d/%m/%Y').date()
                except ValueError:
                    print(f"Format de date invalide: {date_retour}")
                    self.date_retour = None
        else:
            self.date_retour = date_retour

    def saisir_infos_emprunt(self , liste_utilisateurs , liste_livres):
        print("vous êtes sur le point d'enregistrer d'un nouvel emprunt...")
       
        if not  demande_si_continuer():
            return
            # Saisie ID utilisateur
        while True:
            try:
                self.id_utilisateur = int(input("Entrer l'identifiant de l'utilisateur  : "))
                if existe_utilisateur_par_id(self.id_utilisateur , liste_utilisateurs ):
                    break
                else:
                    print("⚠️ Cet utilisateur n'existe pas, réessayez.")
            except ValueError:
                    print("⚠️ Veuillez entrer un identifiant valide.")
        # Saisie ID livre
        while True:
            try:
                self.id_livre = int(input("Entrer l'identifiant du livre a emprunter : "))
                if existe_livre_par_id(self.id_livre , liste_livres):
                        break
                else:
                    print("Ce Livre n'exite pas ...")
            except ValueError:
                print("⚠️ Veuillez entrer un identifiant valide.")
            # Affectation automatique des dates
        self.date_emprunt = date.today()
        self.date_retour =  self.date_emprunt + timedelta(days=14)
            # DECREMENTATION DU NOMBRE D EXEMPLAIRE DU LIVRE   
        for livre in liste_livres:
            if livre.id_livre == self.id_livre:
                if livre.nombre_exemplaire > 1:
                    livre.nombre_exemplaire -= 1
                    break
                else:
                    liste_livres.remove(livre)
                
                    # Génération automatique de l'id_emprunt
                    # self.id_emprunt = generer_id_emprunt()


    def __str__(self):
        # print("DEBUG:", type(self.date_emprunt))  # 🔍 Debug temporaire
        return (
            f"\n🔖 Emprunt ID : {self.id_emprunt}\n"
            f"👤 Utilisateur ID : {self.id_utilisateur}\n"
            f"📖 Livre ID : {self.id_livre}\n"
            
            f"📅 Date d'emprunt : {self.date_emprunt.strftime('%d/%m/%Y')}\n"
            f"📅 Date de retour prévue : {self.date_retour.strftime('%d/%m/%Y')}\n"
        )

                    
                      
                            
                    
        
