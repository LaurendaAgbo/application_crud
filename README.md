# 📦 Application de gestion d’articles

## 📌 Description du projet

Ce projet est une petite application web développée en **Python** avec le framework **Flask**.
Il utilise **SQLAlchemy** pour la gestion de la base de données, **SQLite** comme système de stockage et **Bootstrap** pour la mise en forme de l’interface utilisateur.

L’application permet de gérer des **articles** classés par **catégories** dans un contexte simple de démonstration pédagogique.

---

## ⚙️ Technologies utilisées

* Python 3
* Flask
* SQLAlchemy
* SQLite
* Bootstrap

---

## 🗂️ Fonctionnalités

* Afficher la liste des articles disponibles
* Afficher la catégorie associée à chaque article
* Ajouter un nouvel article
* Modifier un article existant
* Supprimer un article
* Choisir une catégorie existante lors de l’ajout ou de la modification d’un article

La table **categories** est initialisée avec **quelques données par défaut** afin de permettre une utilisation immédiate de l’application.

---

## 🧱 Structure simplifiée du projet

```
project/
│
├── app.py
├── db/
|   ├── init_data.py
│   └── database.py
├── models/
|   ├── __init__.py
│   ├── article.py
│   └── categorie.py
├── templates/
│   ├── index.html
│   ├── ajouter.html
│   └── modifier.html
└── README.md
```

---

## 🚀 Installation / Lancement du projet

### 1️⃣ Prérequis

* Python 3.x installé
* pip (gestionnaire de paquets Python)

---

### 2️⃣ Cloner ou récupérer le projet

```bash
git clone <url_du_projet>
cd project
```

Ou simplement décompresser le dossier du projet.

---

### 3️⃣ Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
```

Activation :

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

---

### 4️⃣ Installer les dépendances

```bash
pip install flask sqlalchemy
```

---

### 5️⃣ Lancer l’application

```bash
python app.py
```

---

### 6️⃣ Accéder à l’application

Ouvrir un navigateur et aller à l’adresse :

```
http://127.0.0.1:5000
```

---

## 🧠 Améliorations possibles

* Permettre à l’utilisateur d’ajouter une **nouvelle catégorie** directement lors de l’ajout ou de la modification d’un article
* Ajouter des validations plus avancées sur les formulaires
* Ajouter un système de recherche ou de filtrage par catégorie
* Séparer davantage la logique métier et les routes

---

## 📚 Objectif pédagogique

Ce projet a pour but de :

* Comprendre les bases de **Flask**
* Manipuler une base de données avec **SQLAlchemy**
* Mettre en place des relations entre tables
* Créer une application CRUD simple
* Structurer correctement un projet web Python

