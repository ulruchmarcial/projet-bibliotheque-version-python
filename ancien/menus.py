
# fonction menu principal
def MenuPrincipal():

            print("\n" + "*" * 120)
            print("*************** BIENVENUE DANS L'APPLICATION: GESTION D'UNE BIBLIOTHÈQUE ***************")
            print("*" * 120)
            print("""
            ============== MENU PRINCIPAL ==============
                        A. Gérer les livres
                        B. Gérer les utilisateurs
                        C. Gérer les emprunts
                        D. Statistiques
                        Q. Quitter
            """)

# fonction Sous-menu Livre
def SousMenuLivre():
        
        print("\n====== GESTION DES LIVRES ======")
        print("1. Ajouter un livre")
        print("2. Rechercher un livre")
        print("3. Afficher la liste des livres")
        print("4. Supprimer un livre")
        print("5. Retour au menu principal")

# fonction Sous-menu Utilisateur
def sous_menu_utilisateurs():
    
        print("\n====== GESTION DES UTILISATEURS ======")
        print("1. Ajouter un utilisateur")
        print("2. Afficher la liste des utilisateurs")
        print("3. Supprimer un utilisateur")
        print("4. Retour au menu principal")

# fonction Sous-menu Emprunts

def sous_menu_emprunts():
    
        print("\n====== GESTION DES EMPRUNTS ======")
        print("1. Emprunter un livre")
        print("2. Retourner un livre")
        print("3. Liste des emprunts")
        print("4. Retour au menu principal")

def SousMenuStatistiques():
   
        print("\n========= STATISTIQUES DE LA BIBLIOTHÈQUE =========")
        print("1. Nombre total de livres")
        print("2. Nombre total d'utilisateurs")
        print("3. Nombre total d'emprunts")
        print("4. Retour au menu principal")
        print("===================================================")



