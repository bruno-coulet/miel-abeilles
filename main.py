from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION, INTERLIGNE, GENERATION_COUNT

def main():

    beehive = Beehive(POPULATION_SIZE)

    print("\nPopulation : ", POPULATION_SIZE, " abeilles\nSelection  : ", SELECTION, " abeilles\n")

    # beehive.generate_bees() EST DEJA DANS LE CONSTRUCTEUR  

    print(f"\nChemins AVANT cross_over:\n") 
    print("beehive.bees : ",beehive.bees)

    # for i in range(GENERATION_COUNT):
    print(f"\nChemins APRES cross_over:\n")    
    beehive.select_bees()
    beehive.cross_bees()


if __name__ == "__main__":
    main()
