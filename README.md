# PalSaver
Script python permettant la sauvegarde de votre serveur Palworld depuis un serveur FTP sur votre machine locale.
Ce script a été développé pour fonctionner avec le serveur Palworld de [Nitroserv](https://www.nitroserv.com/).

## Prérequis
- [Python 3.12](https://www.python.org/downloads/)
- Installation des modules python trouvé dans le fichier `requirements.txt`
  - [pip](https://pip.pypa.io/en/stable/installation/): `python -m pip install -r requirements.txt` ou `pip install -r requirements.txt` si pip est déjà installé

## Installation
Télécharger la dernière release [ici](https://github.com/AlexandreFrancony/PalSaver/releases/).
Extraire le fichier zip dans le dossier de votre choix.
Ouvrir le fichier `.env` et ajouter les valeurs nescessaire.
Dans le cas d'un serveur Nitroserv, les valeurs sont de cette forme:
```
HOSTNAME="ftp.nitroserv.games"
USERNAME_SERVER="<ID>-<Nom>"
PWD="***********"
REMOTE_PATH="/Palworld/Pal/Saved"
LOCAL_PATH="C:\Users\Saves_Palworld" # Par exemple
```
Ensuite, il faut modifier le fichier `launch.bat` (clique droit, ouvrir avec Bloc-Notes) afin de compléter le chemin du script:
```
@echo off
cd <Chemin du dossier du script>
python src/main.py
```

## Utilisation
Lancer le fichier `launch.bat`.<br>
Le script va créer un dossier `Saves_Palworld` dans le dossier spécifié dans le fichier `.env`.<br>
Le script va ensuite télécharger les fichiers de sauvegarde du serveur FTP dans le dossier `Saves_Palworld`.<br>
A noter que des logs sont créés dans le dossier `logs` du dossier du `Saves_Palworld`.

## Automatisation
Pour automatiser le script, il faut créer une [tâche planifiée](https://www.malekal.com/les-taches-planifiees-de-windows/#:~:text=Les%20t%C3%A2ches%20planifi%C3%A9es%20de%20Windows,ou%20au%20d%C3%A9marrage%20de%20Windows.) qui va lancer le fichier `launch.bat` à l'heure souhaitée.

## Conclusion
Merci d'avoir lu ce README, j'espère que ce script vous sera utile, il n'est pas parfait, en cas de soucis je resterais vigilent sur ce repo.