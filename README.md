🔍 Contexte

À l'origine, cette tâche était réalisée en Java avec plus de 100 lignes de code, en raison de la gestion manuelle du parsing, des connexions JDBC et des conversions de types.
Ici, le même travail est réalisé en moins de 25 lignes de Python, en combinant :

    Le module csv pour lire le fichier,

    Le module psycopg2 pour interagir avec PostgreSQL,

    Une procédure stockée (importer_donnees) pour l'insertion sécurisée.

⚙️ Prérequis

Avant d'utiliser le script, vous devez disposer de :

    PostgreSQL installé et accessible

    Une base de données avec une procédure stockée nommée importer_donnees, par exemple :

CREATE OR REPLACE PROCEDURE importer_donnees(
    type_maison TEXT,
    commodites TEXT,
    localite TEXT,
    loyer INTEGER,
    telephone TEXT,
    date_publication DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO votre_table (
        type_maison, commodites, localite, loyer, telephone, date_publication
    ) VALUES (
        type_maison, commodites, localite, loyer, telephone, date_publication
    );
END;
$$;

Le fichier CSV avec les colonnes suivantes :

    type_maison

    commodites

    localite

    loyer

    telephone

    date_publication (format YYYY-MM-DD)

Les bibliothèques Python nécessaires :

    pip install psycopg2

📌 Utilisation

    Modifier les paramètres de connexion à votre base PostgreSQL :

conn = psycopg2.connect(
    dbname="votre_base",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    host="localhost",
    port=5432
)

Indiquer le chemin vers le fichier CSV :

with open("chemin/vers/fichier.csv", encoding="utf-8-sig") as f:

Lancer le script :

    python import_csv.py

🛠️ Fonctionnement

Pour chaque ligne du fichier :

    Les données sont extraites et nettoyées (ex. : conversion des types).

    La procédure importer_donnees est appelée.

    En cas d’erreur, la transaction est annulée pour cette ligne et une erreur est affichée.

    Sinon, la transaction est validée (commit).

✅ Avantages

    Code concis, lisible et facilement réutilisable

    Séparation des responsabilités (procédure stockée côté SQL)

    Gestion d’erreurs ligne par ligne

    Compatible avec d'autres SGBD avec peu d’adaptations (ex : MySQL ou Oracle)

💬 Auteurs & Contact

Créé par [Ton Nom ou Ton Pseudo GitHub]
N'hésitez pas à ouvrir une issue ou à me contacter pour toute question ou amélioration !