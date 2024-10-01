import random, math
from constants import FLOWERS, POPULATION_SIZE, SELECTION, REJECTION

class Bee():
    def __init__(self, bee_id, bee_path = [], modified_path = []):
        self.bee_id = bee_id
        self.flowers_list = FLOWERS.copy()
        self.path = bee_path
        self.modified_path = modified_path
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

    def gathering_path(self) -> list[tuple[int, int]]:
        """ Returns the path of flower collection """
        self.path = self.flowers_list
        return self.path
    
    def __repr__(self) -> str:
        return f"Bee id : {self.bee_id}, \nBee path : {self.gathering_path()}\n"

#------------------------------------------------------

memorized_paths = []
generated_bees = []

#---------------------First Generation---------------------------------
class Beehive:
    def __init__(self, population_size, selected=[], modified=[]):
        self.population_size = population_size
        self.selected = selected
        self.modified = modified
        self.generated_bees = []
        self.memorized_paths = []

    def generate_bees(self):
        '''Generates as many bees as defined in population_size'''
        self.generated_bees = [Bee(i) for i in range(self.population_size)]
        return self.generated_bees


    def sorted_distances(self) -> list[tuple[float, Bee]]:
        """Tuples (distance, bee), sorted by the distance."""
        if not self.generated_bees:
            self.generate_bees()  # Ensure bees are generated
        distances_with_bees = [(bee.total_distance(), bee) for bee in self.generated_bees]
        return sorted(distances_with_bees, key=lambda x: x[0])
    # print(sorted_distances())


    self.sorted_bees = sorted_distances()




    def selected_bees(SELECTION) -> list[Bee]:
        sorted_bee_distances = self.sorted_distances() 
        return [bee for _, bee in sorted_bee_distances[:SELECTION]]

    def rejected_bees(REJECTION) -> list[Bee]:
        rejected_bee_distances = sorted_distances()
        return [bee for _, bee in rejected_bee_distances[-REJECTION:]]

    def selected_paths(SELECTION) -> list[Bee]:
        ''' lists the paths of the best bees '''
        selected_paths = []
        chosen_bees = selected_bees(SELECTION)
        for bee in chosen_bees:
            selected_paths.append(bee)
            memorized_paths.append(bee.gathering_path())
        return selected_paths
    # print("\nselected_paths (liste d'objets bee):\n\n", selected_paths(SELECTION))



    #-----------------------Modifications--------------------------------------------


    def modify_first_to_last(self, selected_bees: list[Bee]) -> list[Bee]:
        modified_bees = []
        for bee in selected_bees:
            # creates a shallow copy of the path
            path = bee.gathering_path()[:]
            path[0], path[-1] = path[-1], path[0]
            # Assign modified path to the bee
            bee.modified_path = path
            modified_bees.append(bee)
        return modified_bees


# ------------------------Second generation----------------------------------------

# Ne pas changer les 50 meilleurs abeilles
# la 51eme prend le chemin de la première et swape la 1ère et la dernière fleur
# la 52eme prend le chemin de la 2ère et swape la 1ère et la dernière fleur
#  etc...




