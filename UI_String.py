# PROGRAM
PROGRAM_VERSION = "0.0.1a"
PROGRAM_HEADER = """
-----------------------------------------------------------------
|                                                               |
|    Logiciel de gestion d'employé et de création d'horraire    |
|                        Version {}                         |
|                   Par: Samuel Martel - 2018                   |
|                                                               |
-----------------------------------------------------------------
""".format(PROGRAM_VERSION)
PROGRAM_HELP_INFO = "Pour voir les commandes discponibles, utiliser la commande d'aide [?]\n"
UNHANDLED_EXCEPTION = """Une erreur non-gérée de type {} est survenu.
Détails:
{}
"""

# DATA
DATA_EMPLOYE_SAVED = "Données des employés sauvegardé!"

# SESSION
SESSION_LOGIN_CODE = "Veuillez entrer votre numéro d'employé: "
SESSION_LOGIN_PW = "Veuillez entrer votre mot de passe: "
SESSION_NO_USER_ERROR = "Aucun employé n'est enregistré, pour continuer, veuillez ajouter un employé à la base de " \
                        "donnée. "
SESSION_CONFIRM_USER_CREATION = "Désirez vous en ajouter un maintenant? (Votre accès sera limité si vous ne vous " \
                                "connectez pas) [o/n]: "

# USERS
USERS_CREATION_HEADER = "--- Création d'un utilisateur ---".upper()
USERS_CREATION_VERIFICATION = "Voici les informations entrée: "
USERS_IS_INFO_GOOD = """Est-ce que les informations entrées sont correcte?
Si oui, écrivez 'oui'
Sinon, écrivez le nom du champs à modifier: """
USERS_FIELD_NOT_EXIST = "Ce champ n'existe pas."
USERS_ABOUT_TO_DELETE_ALL = "Vous êtes sur le point de suprimer {} employés. Cette action n'est pas réversible"
USERS_CONFIRMATION_DELETE = "Voulez-vous continuer? [o/n]: "
USER_DATA_DELETED = "Données effacées."
USERS_FIELD_INVALID = "Incapable de trier les employés par '{}'"
USERS_NOT_FOUND = "Aucun employé ne correspond à cette recherche."
USERS_FOUND = "--- RÉSULTAT ---"
USERS_NO_DATA = "Aucun employé."
# USERS_CODE
USERS_GET_CODE = "- Code de l'employé: "
USERS_CODE_INFO = "Code que l'employé va utilisé pour l'horodateur"
USERS_CODE_NOT_GOOD = "ERREUR: Le code d'employé doit être composé de 4 chiffres"
USERS_CODE_ALREADY_ASSIGNED = "ERREUR: Le code '{}' est déjà assigné à un employé, voulez-vous continuer? [o/n]: "
# USERS_NAME
USERS_GET_NAME = "- Prénom de l'employé: "
USERS_NAME_INFO = "Chacun des noms personnels qui précèdent le nom de famille de l'employé."
USERS_NAME_NOT_GOOD = "ERREUR: ce champs ne peut pas contenir de chiffre"
# USERS_SURNAME
USERS_GET_SURNAME = "- Nome de famille de l'employé: "
USERS_SURNAME_INFO = "Patronyme. Nom qui suit ou devance le prénom. Le nom de famille est inscrit dans l'état civil, " \
                     "il correspond au nom d'un des deux parents, ou des deux (ils peuvent être accolés). Il est " \
                     "transmis de génération en génération. "
# USERS_PIN
USERS_GET_PIN = "Mot de passe de l'employé: "
USERS_PIN_INFO = "Mot de passe à 5 chiffres afin d'acceder au compte utilisateur de ce logiciel"
USERS_PIN_NOT_GOOD = "ERREUR: Le mot de passe ne doit contenir que 5 chiffres"
# USERS_POSTE
USERS_GET_POSTE = "Poste de l'employé: "
USERS_POSTE_INFO = """
Poste que l'employé va être.
Peut être:
	- cuisine
	- caisse
	- responsable
	"""
USERS_POSTE_NOT_GOOD = """ERREUR: Le poste doit être un des postes suivants:
	- cuisine
	- caisse
	- responsable"""
# USERS_FORMATION
USERS_GET_FORMATION = "Poste où l'employé est formé: "  # TODO Trouver un meilleur terme que "Poste"
USER_FORMATION_INFO = """Formation dont l'employé dispose selon le poste où il se trouve.
Si l'employé a plusieurs formations, veuillez les séparer par ', '.
Peut être:
	- Dans la cuisine:
		- frite
		- panier
		- sauce
		- fromage
		- panne
		- table
		- 1
		- pizza
		- sortie
		- étirage
	- Au caisse:
		- base
		- call
		- dispatch
	- Responsable:
		- whatever a responsable is supposed to do
		"""
# TODO Obtenir les postes via un fichier externe
# TODO Clarifier les responsabilités/formations possible pour tout les postes
USERS_FORMATION_NOT_GOOD = "ERREUR: La/les formations entrées ne sont pas correcte"
# USERS_DATE
USERS_GET_DATE = "Date d'embauche de l'employé [JJ/MM/AAAA]: "
USERS_DATE_INFO = "Date à laquelle l'employé a été engagé."
USERS_DATE_NOT_GOOD = "ERREUR: La date entrée n'est pas valide, est-elle bien sous le format [JJ/MM/AAAA] ?"
USERS_DATE_NOT_VALID = "ERREUR: La valeure entrée n'est pas une date."
USERS_DATE_IN_THE_FUTURE = "ERREUR: La date d'embauche ne peut pas être dans le future."
# USERS_SALARY
USERS_GET_SALARY = "Salaire de l'employé: "
USERS_SALARY_INFO = "Salaire horraire de l'employé en $CAN/h. Doit être supérieur ou égal à 11.25"
USERS_SALARY_NOT_GOOD = "ERREUR: Le salaire entrée n'est pas valide."
USERS_SALARY_BELLOW_MINIMUM = "ERREUR: Le salaire doit être supérieur au salaire minimum."
# USERS_DISPO
USERS_GET_DISPO = "Disponibilitées pour les {}: "
USERS_DISPO_INFO = """Disponibilitées de l'employé pour chaque jours de la semaine.
Les valeurs possible sont:
	- ND: Non-disponible
	- oui: Toute la journée
	- matin: Disponible de 8h30 jusqu'à 14h
	- midi: Disponible de 11h jusqu'à 14h
	- journée: Disponible de 11h jusqu'à 19h
	- soir: Disponible de 16h  jusqu'à 21h
	- close: Disponible de 17h jusqu'à la fermeture
Si vous désirez entrer plusieurs valeures, veuillez les séparer par ', '
"""
USERS_DISPO_NOT_GOOD = "La disponibilitée entrée n'est pas valide"
# USERS_PRIORITY
USERS_GET_PRIORITY = "Priorité de l'employé: "
USERS_PRIORITY_INFO = "Priorité de l'employé lors de la création d'horraire."
USERS_PRIORITY_NOT_GOOD = "Cette valeure n'est pas valide."

# COMMAND
CMD_NOT_AVAILABLE = "Cette commande n'est pas disponible, pour voir toutes commandes disponible, utilisez la commande " \
                    "AIDE. "
CMD_NOT_VALIDE = "ERREUR: Cette commande nécéssite {} paramètre(s)."

# SCHEDULE
SCHEDULE_TEMPLATE_NOT_FOUND = "Le fichier d'horraire de base n'a pas été trouvé, création de ce fichier."
SCHEDULE_COULDNT_FIND_SETTING_FILE = "Le fichier d'option de création d'horraire n'a pas été touvé, veuillez en créer " \
                                     "un. "
SCHEDULE_SETTING_IS_EMPTY = "Le fichier d'option est vide, veuillez le remplir."
