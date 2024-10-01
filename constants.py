import csv

def list_flowers():
    flowers = []

    with open('data/fleurs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # skips the header
        next(reader)
        # adds the coordinates tuple in the flowers list
        for row in reader:
            x = int(row[0])
            y = int(row[1])
            flowers.append((x, y))
    return flowers

FLOWERS = list_flowers()
POPULATION_SIZE = 12
SELECTION = 6
REJECTION = 6
INTERLIGNE = "-"*80
GENERATION_COUNT =10
