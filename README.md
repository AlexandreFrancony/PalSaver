# PalSaver
Script python permettant la sauvegarde de votre serveur Palworld depuis un serveur FTP sur votre machine locale.<br>
Ce script a été développé pour fonctionner avec le serveur Palworld de [Nitroserv](https://www.nitroserv.com/).

## Prérequis
- [Python 3.12](https://www.python.org/downloads/)
> [!TIP]
> Si c'est la première fois que vous installez Python, vous devrez relancer votre ordinateur afin que le script fonctionne !
- Installation des modules python trouvé dans le fichier `requirements.txt` (à voir après grâce au easy setup)

## Installation
Télécharger la dernière release [ici](https://github.com/AlexandreFrancony/PalSaver/releases/).<br>
Extraire le fichier zip dans le dossier de votre choix.<br>

Vous avez maintenant 2 options pour installer les modules python nécessaires au fonctionnement du script et remplir vos identifiants : via l'easy setup ou manuellement.

### Easy setup

Pour lancer le easy setup, il faut lancer le fichier `setup.bat` se trouvant dans le dossier nouvellement extrait. Ce easy setup vous aidera à :
1) Remplir le fichier `.env` avec vos identifiants de connexion.
2) Télécharger les bibliothèques requises au bon fonctionnement du script.
Une fois ce setup terminé, vous pouvez passer à l'utilisation du script.

### Manuellement

Ouvrir le fichier `.env` et ajouter les valeurs nécessaires :
 - `HOSTNAME` : Nom de domaine du serveur FTP (pour Nitroserv, c'est `ftp.nitroserv.games`)
 - `USERNAME_SERVER` : Identifiant du serveur FTP (pour Nitroserv, c'est trouvable sous l'onglet 'Comptes FTP' du manager)
 - `PWD` : Mot de passe du serveur FTP (Mot de passe définit avec le Username dans l'onglet 'Comptes FTP' du manager)
 - `REMOTE_PATH` : Chemin du dossier de sauvegarde sur le serveur FTP (pour Nitroserv, c'est `/Palworld/Pal/Saved`)
 - `LOCAL_PATH` : Chemin du dossier où vous souhaitez sauvegarder votre save (par exemple `C:\Saves_Palworld`)
 - `RCON_IP` : Adresse IP du serveur (pour Nitroserv, c'est trouvable dans l'onglet 'Mon serveur' du manager, dans la partie gauche de l'écran, SANS LA PARTIE APRÈS LES DEUX POINTS)
 - `RCON_PORT` : Port RCON du serveur (pour Nitroserv, c'est trouvable dans l'onglet 'Mon serveur' du manager, dans la partie droite de l'écran, avec le RCON password, par défaut 9221 chez Nitroserv)
 - `RCON_PWD` : Mot de passe RCON du serveur (pour Nitroserv, c'est trouvable dans l'onglet 'Mon serveur' du manager, dans la partie droite de l'écran)

## Utilisation
Lancer le fichier `launch.bat`.<br>
Le script va télécharger les fichiers de sauvegarde du serveur FTP dans le dossier spécifié dans la variable `LOCAL_PATH` du fichier `.env`<br>
À noter que des logs sont créés dans le dossier `logs` du dossier du `Saves_Palworld`.

## Automatisation
Pour automatiser le script, il faut créer une [tâche planifiée](https://www.malekal.com/les-taches-planifiees-de-windows/#:~:text=Les%20t%C3%A2ches%20planifi%C3%A9es%20de%20Windows,ou%20au%20d%C3%A9marrage%20de%20Windows.) qui va lancer le fichier `launch.bat` à l'heure souhaitée.

## Conclusion
Merci d'avoir lu ce README, j'espère que ce script vous sera utile, il n'est pas parfait, en cas de soucis, je resterais vigilant sur ce repo.