import random, math
from constants import FLOWERS, POPULATION_SIZE, SELECTION, REJECTION

class Bee():
    def __init__(self, bee_id, bee_distance = 0, bee_path = [], modified_path = []):
        self.bee_id = bee_id
        self.flowers_list = FLOWERS.copy()
        self.distance = bee_distance
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


#---------------------First Generation---------------------------------
class Beehive:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generated_bees = []
        self.memorized_paths = []

    def generate_bees(self):
        '''Generates as many bees as defined in population_size'''
        self.generated_bees = [Bee(i) for i in range(self.population_size)]
        return self.generated_bees

    def sorted_bees(self) -> list[tuple[float, Bee]]:
        """Tuples (distance, bee object), sorted by the distance."""
        if not self.generated_bees:
            self.generate_bees()
        distances_with_bees = [(bee.total_distance(), bee) for bee in self.generated_bees]
        return sorted(distances_with_bees, key=lambda x: x[0])

    def selected_bees(self) -> list[Bee]:
        sorted_bee_distances = self.sorted_bees()
        return [bee for _, bee in sorted_bee_distances[:SELECTION]]

    def rejected_bees(self) -> list[Bee]:
        rejected_bee_distances = self.sorted_bees()
        return [bee for _, bee in rejected_bee_distances[-REJECTION:]]
    
    def selected_paths(self) -> list[Bee]:
        ''' lists the paths of the best bees '''
        selected_paths = []
        chosen_bees = self.selected_bees()
        for bee in chosen_bees:
            selected_paths.append(bee)
            self.memorized_paths.append(bee.gathering_path())
        return selected_paths



    #-----------------------Modifications--------------------------------------------

    def mutation_first_to_last(self, selected_bees: list[Bee]) -> list[Bee]:
        modified_bees = []
        for bee in selected_bees:
            # creates a shallow copy of the path
            path = bee.gathering_path()[:]
            path[0], path[-1] = path[-1], path[0]
            # Assign modified path to the bee
            bee.modified_path = path
            modified_distance = bee.total_distance()
            modified_bees.append(bee)
        return modified_bees, modified_distance

    def generate_random_positions(self):
        random_positions = []
        for i in range(2):
            r = random.randint(1,len(self.memorized_paths[0]))
            random_positions.append(r)
        return random_positions

    def mutation_random_positions(self, selected_bees: list[Bee]) -> list[Bee]:
        modified_bees = []
        position = self.generate_random_positions()
        for bee in selected_bees:
            # creates a shallow copy of the path
            path = bee.gathering_path()[:]
            path[position[0]], path[position[1]] = path[position[1]], path[position[0]]
            # Assign modified path to the bee
            bee.modified_path = path
            modified_bees.append(bee)
        return modified_bees

# ------------------------Second generation----------------------------------------

# Ne pas changer les 50 meilleurs abeilles
# la 51eme prend le chemin de la première et swape la 1ère et la dernière fleur
# la 52eme prend le chemin de la 2ère et swape la 1ère et la dernière fleur
#  etc...




