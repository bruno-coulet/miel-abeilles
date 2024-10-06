from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER
import matplotlib.pyplot as plt


def main():
    # The Beehive constructor generates the bees
    beehive = Beehive(POPULATION_SIZE)

    # Therefore 'bees' objects are generated
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

    # Loop to generate several generations
    for cycle in range(CYCLE_NUMBER):
        print(f"--- Génération {cycle + 1} ---")

        beehive.cross_bees()

        # beehive.mutate_first_to_last(beehive.bees)

        # Selects the bees after cross over
        beehive.select_bees()


        average_distance = beehive.average_distance()
        average_distances.append(average_distance)

        best_bee = beehive.bees[0]
        best_distances.append(best_bee.distance)
        print(f"Meilleure distance après croisement : {best_bee.distance}, Distance moyenne : {average_distance}")


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
