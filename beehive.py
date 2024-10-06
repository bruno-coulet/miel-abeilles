import random, math
from constants import FLOWERS, POPULATION_SIZE, SELECTION_RATE, SELECTED_BEES

class Bee:
    def __init__(self, bee_distance=0, bee_path=[]):
        self.path = FLOWERS.copy()
        random.shuffle(self.path)
        self.compute_distance()

    def distance_a_to_b(self, a, b) -> float:
        """Calculates the Euclidean distance between two points."""
        return round(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2), 2)

    def compute_distance(self) -> float:
        """Calculates the total distance from the hive, through every shuffled flower, and back to the hive."""
        hive = (500, 500)
        current_position = hive
        total_distance = 0

        for flower in self.path:
            total_distance += self.distance_a_to_b(current_position, flower)
            current_position = flower

        # Retour à la ruche
        total_distance += self.distance_a_to_b(current_position, hive)
        self.distance = round(total_distance, 2)

class Beehive:
    def __init__(self, population_size, mutation_rate=0.1):  # Ajout du taux de mutation
        self.population_size = population_size
        self.mutation_rate = mutation_rate  # Stocker le taux de mutation
        self.generate_bees()

    def generate_bees(self) -> None:
        """Génère la population initiale de 'population_size' abeilles"""
        self.bees = [Bee() for _ in range(self.population_size)]

    def select_bees(self) -> None:
        """Trie les abeilles en fonction de leur distance et garde les meilleures."""
        self.bees.sort(key=lambda bee: bee.distance)
        self.bees = self.bees[:int(SELECTED_BEES)]

    def cross_2_bees(self, parent_1: Bee, parent_2: Bee):
        """Croisement entre deux abeilles"""
        middle = len(parent_1.path) // 2
        child_path = parent_1.path[:middle]

        for flower in parent_2.path:
            if flower not in child_path:
                child_path.append(flower)

        child = Bee()
        child.path = child_path
        child.compute_distance()
        return child

    def cross_bees(self):
        """Croisement des abeilles sélectionnées pour générer une nouvelle population"""
        new_bees = []
        for i in range(len(self.bees) - 1):
            parent_1 = self.bees[i]
            parent_2 = self.bees[i + 1]
            child = self.cross_2_bees(parent_1, parent_2)
            
            # Appliquer une mutation aléatoire avec une probabilité `mutation_rate`
            if random.random() < self.mutation_rate:
                self.mutate_swap(child)
            
            new_bees.append(child)
        
        # Compléter la population jusqu'à POPULATION_SIZE avec les enfants générés
        while len(new_bees) < POPULATION_SIZE:
            parent_1 = random.choice(self.bees)
            parent_2 = random.choice(self.bees)
            child = self.cross_2_bees(parent_1, parent_2)
            
            # Appliquer une mutation aléatoire avec une probabilité `mutation_rate`
            if random.random() < self.mutation_rate:
                self.mutate_swap(child)

            new_bees.append(child)

        self.bees = new_bees

    def mutate_swap(self, bee: Bee):
        """Mutation simple qui échange deux fleurs dans le chemin"""
        i, j = random.sample(range(len(bee.path)), 2)
        bee.path[i], bee.path[j] = bee.path[j], bee.path[i]
        bee.compute_distance()

    def average_distance(self) -> float:
        """Calculates the average distance of all bees in the hive"""
        group_distance = sum(bee.distance for bee in self.bees)
        medium_distance = round(group_distance / len(self.bees), 2)
        print(f"Distance moyenne : {medium_distance}")
        return medium_distance

def genetic_algorithm(number_of_generations, mutation_rate=0.1):
    """Algorithme génétique exécutant plusieurs générations."""
    beehive = Beehive(POPULATION_SIZE, mutation_rate)

    for generation in range(number_of_generations):
        print(f"--- Génération {generation + 1} ---")

        # Sélection des meilleures abeilles
        beehive.select_bees()
        print(f"Meilleure distance après sélection : {beehive.bees[0].distance}")

        # Calculer et afficher la distance moyenne des abeilles
        beehive.average_distance()

        # Croisement des abeilles pour former une nouvelle génération
        beehive.cross_bees()

    # Retourner la meilleure solution trouvée
    best_bee = beehive.bees[0]
    print(f"Meilleure solution trouvée : {best_bee.path}, Distance : {best_bee.distance}")
    return best_bee


