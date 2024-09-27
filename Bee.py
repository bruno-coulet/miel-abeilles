import random, math, csv

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

class Bee():
    def __init__(self, bee_id, bee_path = []):
        self.bee_id = bee_id
        self.flowers_list = FLOWERS.copy()
        self.path = bee_path
        random.shuffle(self.flowers_list)
    
    def distance_a_to_b(self ,a ,b):
        """Calculates the Euclidean distance between two points."""
        stage_distance = round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2),2)
        return stage_distance

    def total_distance(self):
        """Calculates the total distance from the hive, through every shuffled flower,back to the hive."""
        hive = (500, 500)
        current_position = hive
        total_distance = 0

        for flower in self.flowers_list:
            stage_distance = self.distance_a_to_b(current_position, flower)
            total_distance += stage_distance
            current_position = flower
        
        return_to_hive_distance = self.distance_a_to_b(current_position, hive)
        total_distance += return_to_hive_distance
        total_distance = round(total_distance,2)
            
        # print(f"\n'total_distance'-> Distance totale parcourue : {total_distance}")
        return total_distance

    def gathering_path(self):
        """ Returns the path of flower collection """
        self.path = self.flowers_list
        # print(f"\ngathering_path : {self.path}")
        return self.path
    



