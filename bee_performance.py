import matplotlib.pyplot as plt


def bee_performance(cycle_number, average_distances, best_distances):
    """
    Plot the performance of the bees.

    :param cycle_number: Number of generations (CYCLE_NUMBER)
    :param average_distances: List of average distances per generation
    :param best_distances: List of best distances per generation
    """
    plt.plot(
        range(cycle_number + 1),
        average_distances,
        marker="o",
        linestyle="-",
        color="b",
        label="Average distance",
    )
    plt.plot(
        range(cycle_number + 1),
        best_distances,
        marker="x",
        linestyle="--",
        color="r",
        label="Best distance",
    )

    plt.title("Evolution of Swarm Performance")
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.legend()
    plt.grid(True)
    plt.show()
