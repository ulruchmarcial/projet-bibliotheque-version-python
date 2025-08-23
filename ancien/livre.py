from utilitaires import demande_si_continuer
class Livre:

    def __init__(self,id = 0, 
                 titre ="", 
                 auteur =" ",
                 annee_de_publication=0 ,
                 genre ="",
                 nombre_exemplaire = 0 ):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee_de_publication = annee_de_publication
        self.genre = genre
        self.nombre_exemplaire  = nombre_exemplaire

    # fonction pour l'enregistrement d'un nouveau livre 

    def SaisirInfosLivre(self):
        print("vous êtes sur le point d'enregistrer d'un nouveau Livre...")
        if demande_si_continuer():
            while True:
                try:
                    self.id = int(input ("Entrer l'identifiant du livre (entre 0 et 100) :  "))
                    if self.id < 1 or self.id > 100:
                        print(" vous devez entrer un identifiant compris entre 0 et 100. réessayez ")
                    else:
                        break 
                except ValueError:
                    print(" vous devez entrer un identifiant valide réessayez. ")
            
            self.titre = input("Entrer le titre du livre : ").strip()
            self.auteur = input("Entrer l'auteur du livre : ").strip()

            while True:
                try:
                    self.annee_de_publication = int(input ("entrer l'anneé de publication du livre :  "))
                    break
                except ValueError:
                    print(" vous devez entrer une anneé  valide. réessayez ")

            self.genre = input("entrer le genre du livre : ").strip()

            while True:
                try:
                    self.nombre_exemplaire = int(input ("entrer le nombre d'exemplaire de ce livre :  "))
                    break
                except ValueError:
                    print(" vous devez entrer un nombre valide . réessayez ")
            # print("  livre enregistré avec success !  ")
    
    # fonction pour l'affichage un livre   
    def __str__(self):
        return f"id : {self.id}, Titre : {self.titre}, Auteur : {self.auteur}, Annee_de_publication : {self.annee_de_publication}, Genre : {self.genre}, Nombre_exemplaire : {self.nombre_exemplaire}"
    
  