import pandas as pd

# url = 'https://docs.google.com/spreadsheets/d/1_XEM6RJGHj2KTNvYBVOcgoOibq9i9YEn/edit?gid=702524072#gid=702524072'

# Lire le fichier CSV dans le même dossier
champs_df = pd.read_csv('../data/champs.csv')

# Afficher le tableau de données
print(champs_df)