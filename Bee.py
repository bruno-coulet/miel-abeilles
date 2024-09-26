import random, math, csv



def list_flowers():

    flowers = []

    with open('data/fleurs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Sauter l'en-tête du CSV s'il y en a un
        next(reader)
        # Pour chaque ligne, lire les coordonnées x, y
        for row in reader:
            x = int(row[0])
            y = int(row[1])
            # Ajouter les coordonnées sous forme de tuple dans la liste
            flowers.append((x, y))

    return flowers


FLOWERS = list_flowers()

class Bee():
    def __init__(self):
        self.flowers_list = FLOWERS.copy()
                # Mélanger la liste de fleurs lors de l'initialisation de chaque abeille
        random.shuffle(self.flowers_list)
    

    def distance_a_to_b(self ,a ,b):
        """Calculates the Euclidean distance between two points."""
        stage_distance = round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2),2)
        return stage_distance

    def gathering_distance(self):
        """Calculates the total distance from the hive, through every shuffled flower,back to the hive."""
        hive = (500, 500)
        current_position = hive
        total_distance = 0

        # print (self.flowers_list)
        for flower in self.flowers_list:
            stage_distance = self.distance_a_to_b(current_position, flower)
            total_distance += stage_distance
            current_position = flower
        
        return_to_hive_distance = self.distance_a_to_b(current_position, hive)
        total_distance += return_to_hive_distance
        total_distance = round(total_distance,2)
            
        # print(f"\n'gathering_distance'-> Distance totale parcourue : {total_distance}")
        return total_distance

    def gathering_path(self):
        """Prints and returns the path of flower collection in order."""
        path = self.flowers_list
        print(f"\n'gathering_path' ->  Les fleurs ont été butinées dans cet ordre : {path}")
        return path
    
    def one_bee_gathers(self):
        """Generates a random path for the bee's flower collection."""
        distance = self.gathering_distance()
        path = self.gathering_path()

# bee = Bee()
# bee.one_bee_gathers()
# bee2 = Bee()
# bee2.one_bee_gathers()