import matplotlib.pyplot as plt


def bee_best_path(coordinates, best_path):
    """
    Plot the path taken by the best bee.

    :param coordinates: List of coordinates of all flowers [(x1, y1), (x2, y2), ...]
    :param best_path: Path of the best bee, a list of coordinate tuples
    """
    # Add the start and end point (the hive)
    hive = (500, 500)

    # Extract the coordinates of the path
    x_path = [hive[0]] + [coord[0] for coord in best_path] + [hive[0]]
    y_path = [hive[1]] + [coord[1] for coord in best_path] + [hive[1]]

    # Create the plot
    plt.figure(figsize=(8, 8))

    # Plot the flowers
    x_flowers, y_flowers = zip(*coordinates)
    plt.scatter(x_flowers, y_flowers, c="red", label="Flowers")

    # Plot the hive
    plt.scatter(hive[0], hive[1], c="blue", marker="s", s=100, label="Hive")

    # Plot the path taken by the best bee
    plt.plot(
        x_path,
        y_path,
        c="green",
        linestyle="--",
        marker="o",
        label="Path of the Best Bee",
    )

    # Add titles and a grid
    plt.title("Path Taken by the Best Bee")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
