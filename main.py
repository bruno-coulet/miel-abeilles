from bee import Bee, selected_bees, best_paths, rejected_bees
from constants import *

print(INTERLIGNE)

print("\nPopulation : ",POPULATION_SIZE," abeilles")
print("Selection : ",SELECTION," abeilles\n")

print(INTERLIGNE)

print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :\n")
for _, bee in selected_bees(SELECTION): 
    print(f"l'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}")

print(INTERLIGNE)

print(f"\nChemins des {SELECTION} meilleures abeilles :\n")
for bee in best_paths(SELECTION):
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}")
        
print(INTERLIGNE)


print("Elimination : ",REJECTION," abeilles\n")
for _, bee in rejected_bees(REJECTION): 
    print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}")



# print("abeilles rejetées : ", rejected_bees())