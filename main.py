from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION_RATE


def main():

    # generate_bees() IS IN THE Beehive CONSTRUCTOR
    beehive = Beehive(POPULATION_SIZE)

    # Therefore the 'bees' objects are generated 
    print("\nPopulation : ",POPULATION_SIZE," abeilles\nTaux de selection  : ",SELECTION_RATE)

    # And we can print their performances thanks to the __repr__ function of Bee class
    print(f"\nChemins et distances des abeilles AVANT cross_over:\n")
    print(beehive.bees)

    # Sorts and selects the bees according to their distances and the SELECTION RATE
    beehive.select_bees()
    print(f"\nChemins APRES cross_over:\n")
    


    beehive.cross_bees()


if __name__ == "__main__":
    main()
