import csv


def list_flowers():
    flowers = []

    with open("data/mini_fleurs.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        # skips the header
        next(reader)
        # adds the coordinates tuple in the flowers list
        for row in reader:
            x = int(row[0])
            y = int(row[1])
            flowers.append((x, y))
    return flowers


GENERATION_COUNT = 2
FLOWERS = list_flowers()
POPULATION_SIZE = 50
SELECTION_RATE = 0.2
SELECTED_BEES = POPULATION_SIZE * SELECTION_RATE
INTERLIGNE = "-" * 80
