from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION_RATE, INTERLIGNE, GENERATION_COUNT


def main():

    beehive = Beehive(POPULATION_SIZE)

    print(
        "\nPopulation : ",
        POPULATION_SIZE,
        " abeilles\nTaux de selection  : ",
        SELECTION_RATE,
        " abeilles\n",
    )

    # beehive.generate_bees() EST DEJA DANS LE CONSTRUCTEUR
    print(f"\nChemins AVANT cross_over:\n")
    beehive.bees

    # Sorts bees according to their distance
    beehive.select_bees()
    print(f"\nChemins APRES cross_over:\n")
    


    beehive.cross_bees()


if __name__ == "__main__":
    main()
