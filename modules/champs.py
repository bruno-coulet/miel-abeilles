import csv

# Tableau 2D de chaînes vides 1000x1000 
champs = [['' for _ in range(1000)] for _ in range(1000)]

# "ruche" aux coordonnées (500, 500)
champs[500][500] = 'ruche'
hive = champs[500][500]

# Coordonnées des fleurs
with open('data/fleurs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Sauter l'en-tête du CSV s'il y en a un
    next(reader)  
    # Pour chaque ligne, lire les coordonnées x, y
    for row in reader:
        x = int(row[0])
        y = int(row[1])
        # Placer l'élément "fleur" aux coordonnées (x, y)
        champs[x][y] = 'X'








# Afficher une partie du champs pour vérifier l'ajout des fleurs et de la ruche
# for row in champs[495:506]:
#     print(row[495:506])

# print(champs)

# # Afficher uniquement les cellules non vides
# for i in range(len(champs)):
#     for j in range(len(champs[i])):
#         if champs[i][j] != '':  
#             print(f"({i},{j}) : {champs[i][j]}")
