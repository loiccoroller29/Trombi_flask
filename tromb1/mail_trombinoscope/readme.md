# Affichage d'un trombinoscope avec envoi de mails

### variables à modifier :

* fichier mel :
    * self.sender_mail 
    * self.password
* fichier main :
    * creation_bdd.create_trombinoscope(<i>user</i>, <i>password</i>, <i>port</i>)
* fichier requete_personnes : 
    * les informations de connexion
* fichier import_fichier:
    * self.path = os.path.join(self.rep, 'adresses.txt') si besoin pour l'import du fichier adresses.txt


### librairies à installer : 

* flask
* mysql-connector-python

### exécution :

> exécuter le fichier main.py (python3.8)

### principe de fonctionnement : 

* import_fichier importe le fichier adresses.txt
* association_mail_personne récupère les données et les trie pour associer email et personne dans la bdd
* insertion crée une table (personnes2) avec les données triées
* mel envoie un mail
* main lance le programme, importe le fichier d'adresses, trie et insère les données.

* main lance flask
    * index.html affiche les images, le nom, le prénom, l'email
    * des boutons actionnent des formulaires pour le bouton suivant, précédent, envoi de mail

### architecture :

* les fichiers python sont à la racine du site
* les fichiers html sont dans le dossier templates
* les fichiers css et les images sont dans le dossier static