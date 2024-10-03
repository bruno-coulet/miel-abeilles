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
    print("beehive.bees : ", beehive.bees)

    # for i in range(POPULATION_SIZE):
    print(f"\nChemins APRES cross_over:\n")

    beehive.select_bees()
    # print("select_bees() : ",selected)

    crossed = beehive.cross_bees()


if __name__ == "__main__":
    main()
