from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION, INTERLIGNE

def main():
    print(INTERLIGNE)
    print("-" * 36, "main.py", "-" * 36)
    print(INTERLIGNE)

    beehive = Beehive(POPULATION_SIZE)

    print("\nPopulation : ", POPULATION_SIZE, " abeilles")
    print("Selection  : ", SELECTION, " abeilles\n")

    print(INTERLIGNE)

    beehive.generate_bees()

    print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :")

    selected_bees = beehive.selected_bees()
    for bee in selected_bees:
        print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}\n")


    print(INTERLIGNE)


    print(f"\nChemins des {SELECTION} meilleures abeilles :\n")

    selected_paths = beehive.selected_paths()
    for bee in selected_paths:
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}\n")


    print(INTERLIGNE)


    modified_bees = beehive.modify_first_to_last(selected_paths)

    print("\nOriginal paths:\n", [bee.gathering_path() for bee in modified_bees])
    print("\nModified paths:\n", [bee.modified_path for bee in modified_bees])

if __name__ == "__main__":
    main()
