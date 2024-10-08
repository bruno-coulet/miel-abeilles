from beehive import Beehive, genetic_algorithm
from constants import (
    POPULATION_SIZE,
    SELECTION_RATE,
    CYCLE_NUMBER,
    MUTATION_RATE,
    FLOWERS,
    INTERLIGNE,
)
import matplotlib.pyplot as plt
from bee_path import bee_best_path
from bee_performance import bee_performance


def main():
    # Initialize the beehive
    beehive = Beehive(POPULATION_SIZE, MUTATION_RATE)
    print(f"\nPopulation: {POPULATION_SIZE} bees\nSelection rate: {SELECTION_RATE}\n")

    # Run the genetic algorithm
    best_bee, average_distances, best_distances = genetic_algorithm(
        CYCLE_NUMBER, MUTATION_RATE
    )

    print()
    print(INTERLIGNE)
    print()

    # Plot the performance of the bees

    GUI_performance = input(
        "Would you like to see the graph of the best distances and best bees for each generation ? (yes/no) : "
    )
    if GUI_performance in ["yes", "Yes", "YES"]:
        bee_performance(CYCLE_NUMBER, average_distances, best_distances)

    print()
    print(INTERLIGNE)
    print()

    # Plot the path taken by the best bee

    GUI_path = input(
        "Would you like to see the graph of the path of the best bee ? (yes/no) : "
    )
    if GUI_path in ["yes", "Yes", "YES"]:
        bee_best_path(FLOWERS, best_bee.path)


if __name__ == "__main__":
    main()
