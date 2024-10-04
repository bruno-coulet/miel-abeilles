import random, math
from constants import FLOWERS, POPULATION_SIZE, SELECTION_RATE, SELECTED_BEES


class Bee:
    def __init__(self, bee_distance=0, bee_path=[]):
        self.path = FLOWERS.copy()
        random.shuffle(self.path)
        self.compute_distance()

    def distance_a_to_b(self, a, b) -> float:
        """Calculates the Euclidean distance between two points."""
        stage_distance = round(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2), 2)
        return stage_distance

    def compute_distance(self) -> float:
        """Calculates the total distance from the hive, through every shuffled flower,back to the hive."""
        hive = (500, 500)
        current_position = hive
        total_distance = 0

        for flower in self.path:
            stage_distance = self.distance_a_to_b(current_position, flower)
            total_distance += stage_distance
            current_position = flower

        return_to_hive_distance = self.distance_a_to_b(current_position, hive)
        total_distance += return_to_hive_distance
        # total_distance = round(total_distance,2)

        # print(f"\n'total_distance'-> Distance totale parcourue : {total_distance}")
        self.distance = round(total_distance, 2)

    def __repr__(self) -> str:
        return f"\npath : {self.path}, distance : {self.distance}"


# ---------------------First Generation---------------------------------
class Beehive:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generate_bees()

    def generate_bees(self) -> None:
        """Generates as many bees as defined in POPULATION_SIZE"""
        self.bees = [Bee(i) for i in range(self.population_size)]

    def select_bees(self) -> None:  
        """Sorts bees according to their distance
           Selects the top of the list according to the SELECTION RATE"""
        self.bees.sort(key=lambda bee: bee.distance)
        self.bees = self.bees[:int(SELECTED_BEES)]


    # -----------------------Cross over--------------------------------------------

    def cross_2_bees(self, parent_1, parent_2):
        '''reproduce the selected bees'''
        half_path_length = len(parent_1.path)//2
        # child_path gets the first half of parent_1's flowers
        child_path = parent_1.path[:half_path_length]

        # child_path gets the missing flowers in parent_2's path
        for flower in parent_2.path:
            if flower not in child_path:
                child_path.append(flower)
                
        return child_path

    def cross_bees(self):

        for x in range(POPULATION_SIZE - len(self.bees)):
            """Creates a child for each unselected bee
            parents are the selected bees"""

            parent_1 = self.bees[x]
            parent_2 = self.bees[x + 1]
            child_path = self.cross_2_bees(parent_1, parent_2)

            # Create a new Bee with the generated child_path
            child = Bee()
            child.path = child_path
            child.compute_distance()

            # Append the new Bee object to the list of bees
            self.bees.append(child)

            print("parent_1", parent_1)
            print("parent_2", parent_2)
            print("child", child)


            # FOR 50 FLOWERS
            # parent_1_half_1 = parent_1.path[0][0:25]
            # parent_2_half_2 = parent_2.path[1][25:-1]

            # FOR 6 FLOWERS
            # child_path = parent_1.path[:3]
            # for flower in parent_2.path:
            #     if flower not in child_path:
            #         child_path.append(flower)
            # child.path = child_path

            # child_distance = child.compute_distance()
            # print("child_1.path : ", child.path, "\n")
            # print("child_distance : ",child_distance)

        #     child.path = [parent_1_half_1 + parent_2_half_2]

        #     print("child_1\npath = ",child. path,"\ndistance = ",child.distance,"\n")

        #     child_2 = Bee()
        #     # FOR 50 FLOWERS
        #     # parent_1_half_2 = self.memorized_paths[0][25:-1]
        #     # parent_2_half_1 = self.memorized_paths[1][0:25]
        #     # FOR 6 FLOWERS
        #     parent_1_half_2 = self.bees.paths[0][3:]
        #     parent_2_half_1 = self.bees.paths[1][0:3]

        #     child_2.bee_path = [parent_1_half_2 + parent_2_half_1]

        #     print("child_2\npath = ",child_2.bee_path,"\ndistance = ",child_2.distance,"\n")

    # -----------------------Modifications--------------------------------------------

    # def mutate_first_to_last(self, selected_bees: list[Bee]) -> list[Bee]:
    #     modified_bees = []
    #     for bee in selected_bees:
    #         # creates a shallow copy of the path
    #         path = bee.gathering_path()[:]
    #         path[0], path[-1] = path[-1], path[0]
    #         # Assign modified path to the bee
    #         bee.modified_path = path
    #         modified_bees.append(bee)
    #     return modified_bees


# ------------------------Second generation----------------------------------------

# Ne pas changer les 50 meilleurs abeilles
# la 51eme prend le chemin de la première et swape la 1ère et la dernière fleur
# la 52eme prend le chemin de la 2ère et swape la 1ère et la dernière fleur
#  etc...
