from bee import Bee, selected_bees, selected_paths, rejected_bees, memorized_paths, modify_first_to_last
from constants import FLOWERS, POPULATION_SIZE, SELECTION, REJECTION, INTERLIGNE

def main():
    print(INTERLIGNE)
    print("-" * 36, "main.py", "-" * 36)
    print(INTERLIGNE)

    print("\nPopulation : ", POPULATION_SIZE, " abeilles")
    print("Selection  : ", SELECTION, " abeilles\n")

    print(INTERLIGNE)

    print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :")
    for bee in selected_bees(SELECTION):
        print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}\n")

    print(INTERLIGNE)

    print(f"\nChemins des {SELECTION} meilleures abeilles :\n")
    for bee in selected_paths(SELECTION):
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}\n")

    print(INTERLIGNE)

    modified_bees = modify_first_to_last(selected_paths(SELECTION))
    print("\nOriginal paths:\n", [bee.gathering_path() for bee in modified_bees])
    print("\nModified paths:\n", [bee.modified_path for bee in modified_bees])

if __name__ == "__main__":
    main()
