import os

print("Bienvenue dans le programme de configuration de PalSaver !")
print("Ce programme va vous permettre de configurer les variables d'environnement nécessaires au fonctionnement de PalSaver.")
print("Vous pouvez trouver les informations nécessaires sur le manager de votre serveur.\n")
print("Commencer ce processus signifie que le fichier .env sera écrasé.\nSouhaitez vous continuer ? (y/n)")
if input() != "y":
    exit()
print("Début du processus de configuration.\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Demander à l'utilisateur de saisir les valeurs pour chaque variable d'environnement
env_vars = ['HOSTNAME', 
            'USERNAME_SERVER', 
            'PWD', 
            'REMOTE_PATH', 
            'LOCAL_PATH', 
            'RCON_IP', 
            'RCON_PORT', 
            'RCON_PWD'
]

env_comm = {
    "HOSTNAME": "Adresse du serveur FTP",
    "USERNAME_SERVER": "Nom d'utilisateur pour se connecter au serveur FTP",
    "PWD": "Mot de passe du compte pour se connecter au serveur FTP",
    "REMOTE_PATH": "Chemin relatif du dossier de sauvegarde sur le serveur FTP",
    "LOCAL_PATH": "Chemin complet du dossier dans lequel vous souhaitez stocker les sauvegardes en local",
    "RCON_IP": "Adresse IP du serveur RCON",
    "RCON_PORT": "Port du serveur RCON",
    "RCON_PWD": "Mot de passe du serveur RCON"
}

env_values = {
    "HOSTNAME": "ftp.nitroserv.games",
    "USERNAME_SERVER": "",
    "PWD": "",
    "REMOTE_PATH": "/Palworld/Pal/Saved",
    "LOCAL_PATH": "C:\\Saves_Palworld",
    "RCON_IP": "",
    "RCON_PORT": "9221",
    "RCON_PWD": ""
}

new_values = {}

for var in env_vars:
    new_value = ""
    clear()    
    while new_value == "":
        print(f"{var} : {env_comm[var]}\nValeur par défaut : {env_values[var]}\nVeuillez saisir une nouvelle valeur ou appuyer sur Entrée pour conserver la valeur par défaut.")
        new_value = input(var + " = ")
        if new_value != "":
            new_values[var] = new_value
            print("\n")
        elif env_values[var] == "":
            clear()
            print("Vous devez saisir une valeur pour cette variable d'environnement car elle n'a pas de valeur par défaut.\n")
        else :
            new_values[var] = env_values[var]
            new_value = ' '

# Écrire les variables d'environnement dans le fichier .env
with open('.env', 'w') as env_file:
    for var, value in env_values.items():
        env_file.write(f"{var}={value}\n")

clear()
print("Le fichier .env a été rempli avec succès.")

#afficher le contenu du fichier .env
print("\nContenu du fichier .env :")
with open('../.env', 'r') as env_file:
    print(env_file.read())

print("Voulez-vous installer les dépendances du programme ? (y/n)")
if input() == "y":
    try :
        print("Installation des dépendances...")
        os.system("python -m pip install -r ../requirements.txt")
        print("Installation des dépendances terminée.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'installation des dépendances : {e}")