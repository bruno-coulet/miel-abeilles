import random, math, csv
from constants import FLOWERS, POPULATION_SIZE, SELECTION, REJECTION

class Bee():
    def __init__(self, bee_id, bee_path = []):
        self.bee_id = bee_id
        self.flowers_list = FLOWERS.copy()
        self.path = bee_path
        random.shuffle(self.flowers_list)
    
    def distance_a_to_b(self ,a ,b) -> float:
        """Calculates the Euclidean distance between two points."""
        stage_distance = round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2),2)
        return stage_distance

    def total_distance(self) -> float:
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

    def gathering_path(self) -> list[(int, int)]:
        """ Returns the path of flower collection """
        self.path = self.flowers_list
        return self.path
    
    # Dispays bee's informations when the objet is printed
    def __repr__(self) -> str:
        return f"Bee id : {self.bee_id}, \nBee path : {self.gathering_path()}\n"



generated_bees = []

def generate_bees() -> list[Bee]:
    ''' generates as many bees as defined in POPULATION '''
    # Avoid creating a new list of bees if there is one already
    if generated_bees:
        return generated_bees
    # Creates a list of bees if there is none, Use .extend instead of .append to add Bees to the list
    else:
        generated_bees.extend([Bee(i) for i in range(POPULATION_SIZE)])
        return generated_bees
# print(generate_bees())

def sorted_distances() -> list[tuple[float, Bee]]:
    ''' sorts the distances_and_bees list
    shortest distance first, longest distance last'''
    distances_and_bees = [(bee.total_distance(), bee) for bee in generate_bees()]
    sorted_distances = sorted(distances_and_bees, key=lambda x: x[0])
# print(sorted_distances())    
    return sorted_distances

sorted_bees = sorted_distances()


def best_paths(SELECTION) -> list:
    ''' lists the paths of the best bees '''
    best_paths = []
    chosen_bees = selected_bees(SELECTION)
    for distance, bee in chosen_bees:
        # best_paths.append((bee.gathering_path(), bee.bee_id))
        best_paths.append(bee)
    return best_paths


# def worst_paths(REJECTION: int) -> list:
#     ''' lists the paths of the worst bees '''
#     worst_paths = []
#     rejected_bees_list = rejected_bees(REJECTION)
#     for distance, bee in rejected_bees_list:
#         worst_paths.append(bee)
#     return worst_paths



def selected_bees(SELECTION: int) -> list:
    ''' slices the distances_and_bees list according to SELECTION '''
    return sorted_bees[:SELECTION]


def rejected_bees(REJECTION: int) -> list:
    ''' slices the distances_and_bees list according to SELECTION '''
    return sorted_bees[-REJECTION:]







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


