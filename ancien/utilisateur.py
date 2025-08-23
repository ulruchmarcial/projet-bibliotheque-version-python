from utilitaires import demande_si_continuer

class Utilisateur:
    def __init__(self, id=None, nom="", prenom="", adresse="", email="", telephone=""):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.telephone = telephone

    def SaisirInfosUtilisateur(self):
        print("vous êtes sur le point d'enregistrer un nouvel Utilisateur...\n")
        if demande_si_continuer():
            while True:
                try:
                    self.id = int(input("entrer l'identifiant de l'utilisateur : "))
                    if self.id  <= 0 or self.id > 100 :
                        print("l'identifiant doit être entre 1 et 100 : réessayez...")
                    else:
                        break
                except ValueError: 
                    print("Erreur : veillez saisir un identifiant valide (entre 1 et 100) ")
            
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
        return f"id : {self.id}, Nom: {self.nom}, Prenom : {self.prenom}, Adresse : {self.adresse}, Email: {self.email}, Telephone : {self.telephone}"



        

