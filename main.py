from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION, INTERLIGNE, GENERATION_COUNT

def main():


    print("-" * 36, "main.py", "-" * 36)

    for i in range (GENERATION_COUNT):
        beehive = Beehive(POPULATION_SIZE)


        print("\nPopulation : ", POPULATION_SIZE, " abeilles")
        print("Selection  : ", SELECTION, " abeilles\n")
        print(INTERLIGNE)
        print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :\n")

        for bee in beehive.selected_bees(): 
            print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance}\n")


        for bee in beehive.selected_paths():
            print(f"Abeille {bee.bee_id}\n distance {bee.total_distance}\n chemin : {bee.gathering_path()}\n")


        print("-" * 37, "mutation", "-" * 37)


        first_to_last, modified_distances = beehive.mutation_first_to_last(beehive.selected_paths())

        print("\nOriginal paths:\n", [bee.gathering_path() for bee in first_to_last])
        print("\nmutation_first_to_last() Modified paths:\n", [bee.modified_path for bee in first_to_last])
        print("\nmutation_first_to_last() Modified distances:\n", modified_distances)




        # random_position = beehive.mutation_random_positions(beehive.selected_paths())
        # print("\nOriginal paths:\n", [bee.gathering_path() for bee in first_to_last])
        # print("\nmutation_random_position)() Modified paths:\n", [bee.modified_path for bee in first_to_last])

    if __name__ == "__main__":
        main()
