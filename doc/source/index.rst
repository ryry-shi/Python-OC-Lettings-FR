.. oc-lettings-site documentation master file, created by
   sphinx-quickstart on Thu Mar 14 20:44:25 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to oc-lettings-site's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   Usage
   =====

1. Description du projet

   OC-lettings est une application de réservation de bien immobiliers.

2. Installation du projet (pour développement local)

   - Cloner le repository : `git clone https://github.com/ryry-shi/Python-OC-Lettings-FR.git`
   - Se placer dans la branche dev
   - cd dev
   - Créer un fichier .env
   - Y inscrire les variables d'environnement suivantes et les compléter :
      - SENTRY_DSN = <???> (pour lier le projet à Sentry)
      - DJANGO_DEBUG = <???>
      - DJANGO_SECRET_KEY = <???>
      - PORT = 8000
   - docker-compose build
   
3. Guide de démarrage rapide

   - docker-compose up
   - Sur le navigateur tapper : localhost:8000

4. Technologies et les langages de programmation utilisé(e)s

   - Python 3.12.2 comme langage de programmation
   - Django v5 comme dramework web
   - Gunicorn comme serveur d'application
   - Whitenoise comme serveur statique
   - Heroku comme hébergeur
   - Github Actions comme pipeline CI/CD
   - Github comme repository Git

5. Description de la structure de la base de données et des modèles de données

   - Base de données
      Les données sont stockées sur une base de données SQLite3 inclue dans le projet Django.
      Pour consulter votre base de données, vous pouvez exécuter les commandes suivantes sur votre console.

      - cd /path/to/Python-OC-Lettings-FR
      - Ouvrir une session shell sqlite3
      - Se connecter à la base de données .open oc-lettings-site.sqlite3
      - Afficher les tables dans la base de données .tables
      - Afficher les colonnes dans le tableau des profils, pragma table_info (profiles_profile);
      - Lancer une requête sur la table des profils, select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
      - .quit pour quitter

   - Modèles
      Les modèles « Address » et « Letting » sont dans l'application « Lettings »; le modèle « Profile » est dans l'application « Profiles ».

      - Address
         Le modèle « Address » représente une adresse postale.

         Il est constitué de :

            - number : nombre entier positif inférieur à 9 999 correspondant au numéro de la rue
            - street : texte d'une longueur maximale de 64 caractères correspondant au nom de la rue
            - city : texte d'une longueur maximale de 64 caractères correspondant au nom de la ville
            - state : texte d'une longueur de 2 caractères correspondant à l'acronyme de l'Etat
            - zip_code : nombre entier positif inférieur à 99 999 correspondant au code postal
            - country_iso_code : texte d'une longueur de 3 caractères correspondant au code ISO du pays

      - Letting
         Le modèle « Letting » représente un lieu de location.

         Il est constitué de :

         - title : texte d'une longueur maximale de 256 caractères correspondant au titre de la location
         - address : relation un-à-un avec le modèle “Address”

      - Profile
         Le modèle « Profile » représente un profil utilisateur.

         Il est constitué de :

         - user : relation un-à-un avec le modèle “User” par défaut de django
         - favorite_city : texte d'une longueur maximale de 64 caractères correspondant à la ville favorite de l'utilisateur

6. Procédures de déploiement et de gestion de l'application

   - Déploiement : Effectuer une pull request sur master, cela déclenchera le déploiement sur Heroku (via la pipeline Github Actions)
   - Aller sur l'application : https://oc-lettings-app-ryad-a1f52856a169.herokuapp.com/
   - Gestion de l'application : https://oc-lettings-app-ryad-a1f52856a169.herokuapp.com/admin/


===================================
.. note::

   This project is under active development.