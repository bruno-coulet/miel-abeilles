from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION, INTERLIGNE

def main():

    print("-" * 36, "main.py", "-" * 36)

    beehive = Beehive(POPULATION_SIZE)
    beehive.generate_bees()

    print("\nPopulation : ", POPULATION_SIZE, " abeilles")
    print("Selection  : ", SELECTION, " abeilles\n")
    print(INTERLIGNE)
    print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :")

    for bee in beehive.selected_bees(): 
        print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}\n")

    print(INTERLIGNE)

    print(f"\nChemins des {SELECTION} meilleures abeilles :\n")

    for bee in beehive.selected_paths():
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}\n")


    print("-" * 37, "mutation", "-" * 37)


    modified_bees = beehive.mutation_random_positions(beehive.selected_paths())

    print("\nOriginal paths:\n", [bee.gathering_path() for bee in modified_bees])
    print("\nModified paths:\n", [bee.modified_path for bee in modified_bees])

if __name__ == "__main__":
    main()
