from bee import Bee, selected_bees, best_paths
from constants import *


print("\nPopulation : ",POPULATION_SIZE," abeilles\n")
print("Selection : ",SELECTION," abeilles\n")
print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :\n")
#  `_, bee` because `selected_bees` returns a tuple (distance, bee)
for _, bee in selected_bees(SELECTION): 
    print(f"Abeille {bee.bee_id} avec une distance de {bee.total_distance()}")

print(f"\nChemins des {SELECTION} meilleures abeilles :\n\n")

for bee in best_paths(SELECTION):
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}")