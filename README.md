# SchoolDay_Django_project

Ce projet vise à créer un système de gestion de soumissions de projets étudiants en utilisant le framework Django.

## Fonctionnalités

- Module d'inscription et de connexion pour les utilisateurs (étudiant, enseignant, administrateur).
- Chargement/téléchargement d'instructions de projet par les enseignants.
- Soumission de travaux par les étudiants avec évaluation par les enseignants.
- Archivage des projets précédents.
- Gestion des utilisateurs et des rôles.
- Projets ouverts accessibles à tous.

## Prérequis

- Python 3.x
- Django 4.1.x
- MySQL (ou un autre système de gestion de base de données pris en charge)

## Installation

1. Clonez ce dépôt vers votre machine locale :
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

2. Installez les dépendances en utilisant pip :
   pip install -r requirements.txt


3. Configurez la base de données :

- Créez une base de données MySQL avec un nom approprié.
- Mettez à jour les paramètres de base de données dans `settings.py`.

4. Appliquez les migrations pour créer les tables de base de données :
   python manage.py migrate

5. Créez un superutilisateur pour accéder à l'interface d'administration :

python manage.py createsuperuser

6. Lancez le serveur de développement :

python manage.py runserver

7. Accédez au site via votre navigateur à l'adresse [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)

8. Connectez-vous en tant que superutilisateur à [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) pour gérer les utilisateurs et les données.

## Contributeurs

- TAKOUDA Koboyo Grace Abidé


