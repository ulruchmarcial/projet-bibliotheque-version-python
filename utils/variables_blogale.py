import time


from interface.menus import * 
from utils.utilitaires import *
# MenuPrincipal, SousMenuLivre , sous_menu_emprunts , sous_menu_utilisateurs , SousMenuStatistiques , effacer_ecran , quitter_programme , pause
from models.livre import Livre

from  models.utilisateur import Utilisateur
from services.gestion_fichiers import *
from services.gestion_emprunt import *
from services.gestion_livre import *
from services.gestion_utilisateur import *
from services.gestion_statistiques import *
from  models.emprunt import Emprunt


# variables globales

liste_livres = charger_livres()
liste_utilisateurs = charger_utilisateurs()
liste_emprunts = charger_emprunt()
