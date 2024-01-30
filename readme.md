# Projet Horaire Train

## Gestion de Base de Données et Horaire de Train en Python

Ce projet Python propose une application simple pour gérer les horaires de train en utilisant une base de données SQLite. L'application permet d'effectuer des opérations telles que la création de la base de données, l'ajout de trains, la modification d'informations sur les trains existants, et la suppression de trains.

## Structure du Projet

Le projet est organisé en plusieurs classes, chacune représentant une fonctionnalité spécifique.

### `MainDB` (Classe Principale)

- Initialise le chemin de la base de données SQLite.
- Fournit des méthodes utilitaires pour poser des questions à l'utilisateur et se connecter à la base de données.

### `InitDB` (Initialisation de la Base de Données)

- Hérite de `MainDB`.
- Initialise la base de données en exécutant un script SQL d'initialisation.

### `CreateDB` (Création de Trains)

- Hérite de `MainDB`.
- Permet à l'utilisateur d'ajouter des trains en saisissant un code spécifique.

### `ReadDB` (Lecture de la Base de Données)

- Hérite de `MainDB`.
- Actuellement non implémenté (placeholder).

### `UpdateDB` (Modification de Trains)

- Hérite de `MainDB`.
- Permet à l'utilisateur de modifier les informations d'un train existant.

### `DeleteDB` (Suppression de Trains)

- Hérite de `MainDB`.
- Permet à l'utilisateur de supprimer un train de la base de données.

## Utilisation

1. **Création de la Base de Données :**
   - Exécutez le script `InitDB` pour initialiser la base de données avec un script SQL pré-défini.

2. **Ajout de Trains :**
   - Exécutez le script `CreateDB` pour ajouter des trains à la base de données.

3. **Modification de Trains :**
   - Exécutez le script `UpdateDB` pour modifier les informations d'un train existant.

4. **Suppression de Trains :**
   - Exécutez le script `DeleteDB` pour supprimer un train de la base de données.

## Remarques

- Les scripts utilisent une base de données SQLite stockée localement (`data.db`).
- Les codes de train sont générés et vérifiés pour s'assurer qu'ils suivent le format requis.
- Le projet utilise des classes pour encapsuler les différentes fonctionnalités et rendre le code plus modulaire.

## Explication du Code Principal

Le code principal, situé dans un autre fichier, représente une application de gestion d'une base de données pour un projet sur les horaires de train. L'application est divisée en plusieurs classes telles que `App`, qui gère le menu principal, et d'autres classes spécialisées telles que `InitDB`, `CreateDB`, `ReadDB`, `UpdateDB`, et `DeleteDB` qui effectuent des opérations spécifiques sur la base de données.

### Utilisation de l'Application

- L'application propose différentes actions telles que la création de la base de données, l'encodage de données, l'affichage de données, la mise à jour de données, la suppression de données et la sortie de l'application.
- Chaque option du menu est associée à une classe et une méthode spécifiques du module `fn_horaire_train`.

---

*Note : Ce projet est une démonstration éducative et peut nécessiter des adaptations pour être utilisé dans des environnements de production réels.*