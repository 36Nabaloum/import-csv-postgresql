# Import des bibliothèques nécessaires
import csv  # Pour lire les fichiers CSV
import psycopg2  # Pour interagir avec la base de données PostgreSQL
from datetime import datetime  # Pour convertir les dates au bon format

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="loyer_analysis",     # Nom de la base de données
    user="postgres",             # Nom d'utilisateur PostgreSQL
    password="mot de passe",     # Mot de passe (à modifier par votre propre mot de passe)
    host="localhost",            # Hôte (localhost si local)
    port=5432                    # Port par défaut de PostgreSQL
)

# Création d'un curseur pour exécuter les requêtes SQL
cursor = conn.cursor()

# Ouverture du fichier CSV contenant les annonces filtrées
with open("C:/Users/User/OneDrive/Music/annonces_filtrees_20250515_023940.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)  # Lecture ligne par ligne sous forme de dictionnaire

    # Boucle sur chaque ligne du fichier CSV
    for i, row in enumerate(reader, start=1):
        try:
            # Appel de la procédure stockée "importer_donnees" définie dans PostgreSQL
            cursor.execute("""
                CALL importer_donnees(%s, %s, %s, %s, %s, %s);
            """, (
                row['type_maison'],  # Type de logement (ex : villa, appartement)
                row['commodites'],   # Commodités (ex : eau, électricité)
                row['localite'],     # Localisation géographique
                int(row['loyer']) if row['loyer'] else None,  # Loyer (entier ou NULL)
                row['telephone'] if row['telephone'] else None,  # Téléphone (ou NULL)
                datetime.strptime(row['date_publication'], '%Y-%m-%d').date()  # Date au bon format
            ))
        except Exception as e:
            # Gestion des erreurs : impression de l'erreur et rollback de la transaction
            print(f"Erreur ligne {i}: {e}")
            conn.rollback()
        else:
            # Validation de l'insertion si tout s'est bien passé
            conn.commit()

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
