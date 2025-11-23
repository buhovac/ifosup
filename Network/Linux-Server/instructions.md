#Objectif

En binôme, vous allez concevoir et déployer un serveur Linux complet dans
un environnement virtualisé. 
Ce serveur devra offrir des services de
stockage fiable, des partages de fichiers multi-protocoles, et une interface
de gestion à distance.

Cahier des charges
Votre infrastructure doit respecter les spécifications suivantes :
Infrastructure de base

Virtualisation : 
Déployer le serveur sur une machine virtuelle avec réseau
virtuel (pas d’accès par pont, utiliser une mv “cliente”.)

Réseau : 
Configurer une adresse IP fixe pour garantir l’accessibilité
permanente du serveur.

Stockage : 
Mettre en place un système de disques offrant :
• Performances optimisées (au minimum) en lecture ;
• Résistance à la défaillance d’un disque dur ;
• Les disques sont branchables et débranchables à chaud.

Services et accès

Administration distante : 
Permettre la gestion du serveur à distance via :
• Ligne de commande sécurisée ;
• Interface web légère ;

Serveur web Déployer plusieurs protocoles de partage compatibles avec
différents systèmes d’exploitation (Windows, Linux) ainsi qu’un
protocole de partage de fichiers distant.

Gestion des utilisateurs et permissions
Créer les comptes utilisateurs suivants avec leurs droits respectifs :
Espaces de partages
Configurer trois espaces de partage distincts :

1. Public : Accessible en lecture/écriture localement, lecture seule à
   distance, accès anonyme autorisé.
2. Data : Lecture/écriture pour rocky, lecture seule pour anne, inacessible à
   distance.
3. www : Répertoire du serveur web (avec accès FTP pour rocky)
   À rendre
   Vous devez me rendre un rapport de max 10 pages par binôme,
   comprenant :
   • Le nom des deux intervenants ;
   • La documentation technique complète ;
   • Les scripts ou commandes utilisées ;
   • Une courte sitographie des ressources employées.