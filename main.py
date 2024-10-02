from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION, INTERLIGNE, GENERATION_COUNT

def main():

    beehive = Beehive(POPULATION_SIZE)
    print("\nPopulation : ", POPULATION_SIZE, " abeilles\nSelection  : ", SELECTION, " abeilles\n")

    beehive.generate_bees()
    # selected_bees = beehive.selected_bees()

    print(INTERLIGNE)

    print(f"\nChemins des {SELECTION} meilleures abeilles avant cross_over:\n")
    selected_paths = beehive.selected_paths()
    for bee in selected_paths:
        print(f" chemin de l'abeille {bee.bee_id} : {bee.gathering_path()}\ndistance de l'abeille {bee.bee_id} : {bee.total_distance()}\n\n")


    print(INTERLIGNE)


    # for i in range(GENERATION_COUNT):
    print(f"\nChemins apres cross_over:\n")    
    beehive.cross_bees()

        # print("\nOriginal paths:\n", [bee.gathering_path() for bee in modified_bees])
        # print("\nModified paths:\n", [bee.modified_path for bee in modified_bees])

if __name__ == "__main__":
    main()
