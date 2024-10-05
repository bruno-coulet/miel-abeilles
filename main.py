from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER


def main():

    # generate_bees() IS IN THE Beehive CONSTRUCTOR
    beehive = Beehive(POPULATION_SIZE)

    # Therefore the 'bees' objects are generated 
    print("\nPopulation : ",POPULATION_SIZE," abeilles\nTaux de selection  : ",SELECTION_RATE,"\n")

    # # And we can print their performances thanks to the __repr__ function of Bee class
    # print(f"\nChemins et distances des abeilles AVANT cross_over:\n")
    # print(beehive.bees)

    # Sorts and selects the bees according to their distances and the SELECTION RATE
    beehive.select_bees()
    beehive.best_bee()
    beehive.average_distance()

    print(f"\nCROSS OVER:\n")
    

    for _ in range(CYCLE_NUMBER):
        beehive.cross_bees()
        beehive.mutate_first_to_last(beehive.bees)
        beehive.best_bee()
        beehive.average_distance()
    

if __name__ == "__main__":
    main()
