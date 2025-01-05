import kaggle
import os
import pandas as pd

# Le répertoire des informations d'identification de l'API Kaggle
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/Marius KOUAKOU/.kaggle' 

# L'identifiant du jeu de données
dataset = 'piterfm/paris-2024-olympic-summer-games'

# Le chemin de téléchargement
download_path = 'C:/Users/Marius KOUAKOU/OneDrive/Jeux Olympiques Paris 2024/Sources'

# Suppression des fichiers existants dans le dossier pour éviter les doublons ou des fichiers obsolètes
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Supprime le fichier  
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# Téléchargement de l'ensemble de données à l'aide de l'API Kaggle et décompressez les fichiers
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# Liste des fichiers CSV à importer
csv_files = [
    'athletes.csv',
    'events.csv',
    'medallists.csv',
    'medals.csv',
    'medals_total.csv',
    'schedules.csv',
    'schedules_preliminary.csv',
    'teams.csv',
    'torch_route.csv',
    'venues.csv'
]

# Initialisation d'un dictionnaire pour contenir des DataFrames
dataframes = {}

# Parcours chaque fichier CSV et le charge en un DataFrame
for file in csv_files:
    # Construire le chemin complet vers le fichier CSV
    file_path = os.path.join(download_path, file)
    
    # Charge le fichier CSV dans un Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Ajoute le DataFrame au dictionnaire en utilisant le nom du fichier comme clé
    table_name = file.split('.')[0]  # Supprime l'extension .csv  
    dataframes[table_name] = df