from beehive import Beehive, genetic_algorithm
from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER, MUTATION_RATE, FLOWERS
import matplotlib.pyplot as plt
from plot_path import plot_best_path

def main():
    # Initialize the beehive
    beehive = Beehive(POPULATION_SIZE, MUTATION_RATE)
    print(f"\nPopulation: {POPULATION_SIZE} bees\nSelection rate: {SELECTION_RATE}\n")

    # Run the genetic algorithm
    best_bee, average_distances, best_distances = genetic_algorithm(CYCLE_NUMBER, MUTATION_RATE)

    # Plot the performance of the bees
    plt.plot(range(CYCLE_NUMBER + 1), average_distances, marker='o', linestyle='-', color='b', label='Average distance')
    plt.plot(range(CYCLE_NUMBER + 1), best_distances, marker='x', linestyle='--', color='r', label='Best distance')

    plt.title('Evolution of Swarm Performance')
    plt.xlabel('Generation')
    plt.ylabel('Distance')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the path taken by the best bee
    plot_best_path(FLOWERS, best_bee.path)

if __name__ == "__main__":
    main()
