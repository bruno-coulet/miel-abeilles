import random, math, csv
from constants import FLOWERS, POPULATION_SIZE, SELECTION

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
        return self.path
    
    def __repr__(self):
        return f"Bee({self.bee_id}, path={self.gathering_path()})"

generated_bees = []

def generate_bees() -> list:
    ''' generates as many bees as defined in POPULATION '''
    # Avoid creating a new list of bees if there is one already
    if generated_bees:
        return generated_bees
    # Creates a list of bees if there is none
    else:
        # for i in range(POPULATION_SIZE):
        #     generated_bees.append(Bee(i))

        # Use extend or list comprehension to add Bees to the list
        generated_bees.extend([Bee(i) for i in range(POPULATION_SIZE)])
        return generated_bees

        # return [Bee(i) for i in range(POPULATION_SIZE)]
# print(generate_bees())

def sort_distance_list() -> list:
    ''' sorts the distances_and_bees list
    shortest distance first, longest distance last'''
    # sorted_distances = generate_bees().sort()
    # # return sorted_distances

# print(sort_distance_list())

    distances_and_bees = [(bee.total_distance(), bee) for bee in generate_bees()]
    sorted_distances = sorted(distances_and_bees, key=lambda x: x[0])  # Trie par la distance (x[0])
    
    return sorted_distances



def best_paths(SELECTION) -> list:
    ''' lists the paths of the best bees '''
    best_paths = []
    chosen_bees = selected_bees(SELECTION)
    for distance, bee in chosen_bees:
        # best_paths.append((bee.gathering_path(), bee.bee_id))
        best_paths.append(bee)
    return best_paths

def worst_path():
    pass

def selected_bees(SELECTION) -> list:
    ''' slices the distances_and_bees list according to SELECTION '''
    best_bees = sort_distance_list()
    return best_bees[:SELECTION]



def rejected_bees(SELECTION) -> list:
    ''' slices the distances_and_bees list according to SELECTION '''
    rejected_bees = sort_distance_list()
    return rejected_bees[(len(sort_distance_list())-SELECTION):-1]


# On a :
# les meilleurs trajet
# les pires trajets


def cross():
    # Mélanger les meilleurs trajets
    pass

def mutate():
    # objectif : tester différent chemin et les compare
    # assigne les trajets mélangé aux abeilles disponibles 
    best_paths(SELECTION)
    pass

# ? ? ? 
def reproduce():
    pass


