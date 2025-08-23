from utils.utilitaires import demande_si_continuer

class Utilisateur:
    def __init__(self, id_utilisateur=None, nom="", prenom="", adresse="", email="", telephone=""):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.telephone = telephone

    def SaisirInfosUtilisateur(self , liste_utilisateurs):
        print("vous êtes sur le point d'enregistrer un nouvel Utilisateur...\n")
        if demande_si_continuer():
            while True:
                try:
                    self.id_utilisateur = int(input("entrer l'identifiant de l'utilisateur : "))
                    if self.id_utilisateur  <= 0 or self.id_utilisateur > 100 :
                        print("l'identifiant doit être entre 1 et 100 : réessayez...")
                    else:
                        break
                except ValueError: 
                    print("Erreur : veuillez saisir un identifiant valide (entre 1 et 100) ")
            for utilisateur in liste_utilisateurs:
                if self.id_utilisateur == utilisateur.id_utilisateur:
                    print(f"un utilisateur avec l'identifiant {self.id_utilisateur} exite deja !\n  ")
                    print(" veuillez utiliser un autre idetifiant pour enregister un nouvel utilisateur : \n ")
                    if demande_si_continuer():
                        return
                    else :
                        return

            self.nom = input("entrer le nom de l'utilisateur  :  ").strip()
            self.prenom = input("entrer le prénom de l'utilisateur  : ").strip()
            self.adresse = input("entrer  l'adresse  de l'utilisateur  : ").strip()
            self.email = input("entrer l'adresse mail de l'utilisateur  : ").strip()

            while True:
                try:
                    self.telephone = int(input("entrer le numero de telephone de l'utilisateur : "))
                    break
                except ValueError:

                    print("Erreur : veuillez saisir un numero de telephone  valide ")

    def __str__(self):
        return f"id : {self.id_utilisateur}, Nom: {self.nom}, Prenom : {self.prenom}, Adresse : {self.adresse}, Email: {self.email}, Telephone : {self.telephone}"



        

