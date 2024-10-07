from beehive import Beehive, genetic_algorithm
from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER, MUTATION_RATE, FLOWERS
import matplotlib.pyplot as plt
from bee_path import bee_best_path
from bee_performance import bee_performance

def main():
    # Initialize the beehive
    beehive = Beehive(POPULATION_SIZE, MUTATION_RATE)
    print(f"\nPopulation: {POPULATION_SIZE} bees\nSelection rate: {SELECTION_RATE}\n")

    # Run the genetic algorithm
    best_bee, average_distances, best_distances = genetic_algorithm(CYCLE_NUMBER, MUTATION_RATE)

    # Plot the performance of the bees
    bee_performance(CYCLE_NUMBER, average_distances, best_distances)

    # Plot the path taken by the best bee
    bee_best_path(FLOWERS, best_bee.path)

if __name__ == "__main__":
    main()
