from beehive import Beehive, genetic_algorithm

from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER, MUTATION_RATE
import matplotlib.pyplot as plt


def main():

    # The Beehive constructor generates the bees
    beehive = Beehive(POPULATION_SIZE, MUTATION_RATE)
    print(f"\nPopulation : {POPULATION_SIZE} abeilles\nTaux de sélection  : {SELECTION_RATE}\n")

    beehive.select_bees()

    print("\nPerformances avant le cross over:")
    average_distance = beehive.average_distance()
    best_bee = beehive.bees[0]
    print(f"Meilleure distance : {best_bee.distance}\nDistance moyenne : {average_distance}")


    # Stocks distances of each generation
    average_distances = []
    best_distances = []
    average_distances.append(average_distance)
    best_distances.append(best_bee.distance)

    print("\nDÉBUT DU CROSS OVER :\n")

    # Loops to generate several generations
    for cycle in range(CYCLE_NUMBER):
        print(f"--- Génération {cycle + 2} ---")

        beehive.cross_bees()
        beehive.select_bees()

        average_distance = beehive.average_distance()
        best_bee = beehive.bees[0]

        average_distances.append(average_distance)
        best_distances.append(best_bee.distance)

        print(f"Meilleure distance : {best_bee.distance}, Distance moyenne : {average_distance}")

    # genetic_algorithm(CYCLE_NUMBER, MUTATION_RATE)



    print(f"\nMeilleure solution trouvée : {best_bee.path}, Distance : {best_bee.distance}")

    plt.plot(range(CYCLE_NUMBER + 1), average_distances, marker='o', linestyle='-', color='b', label='Distance moyenne')
    plt.plot(range(CYCLE_NUMBER + 1), best_distances, marker='x', linestyle='--', color='r', label='Meilleure distance')

    plt.title('Évolution des performances de l\'essaim')
    plt.xlabel('Génération')
    plt.ylabel('Distance')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
