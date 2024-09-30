from bee import Bee, selected_bees, selected_paths, rejected_bees, memorized_paths, modify_first_to_last
from constants import  FLOWERS, POPULATION_SIZE, SELECTION, REJECTION, INTERLIGNE

print(INTERLIGNE, INTERLIGNE)
print(INTERLIGNE,"Début", INTERLIGNE)
print(INTERLIGNE, INTERLIGNE)


print("\nPopulation : ",POPULATION_SIZE," abeilles")
print("Selection  : ",SELECTION," abeilles\n")

print(INTERLIGNE)

print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :\n")
for bee in selected_bees(SELECTION): 
    print(f"l'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}")


print(INTERLIGNE)

print(f"\nChemins des {SELECTION} meilleures abeilles :\n")
for bee in selected_paths(SELECTION):
        print(f"Abeille {bee.bee_id},\n chemin : {bee.gathering_path()}\n")
        
print(INTERLIGNE)


# print("Elimination : ",REJECTION," abeilles\n")
# for _, bee in rejected_bees(REJECTION): 
#     print(f"L'abeille {bee.bee_id} a parcourue une distance de {bee.total_distance()}, nous allons la remplacer")


modified_bees = modify_first_to_last(selected_paths(SELECTION))
print("\nOriginal paths:\n", [bee.gathering_path() for bee in modified_bees])
print("\nModified paths:\n", [bee.modified_path for bee in modified_bees])

print(INTERLIGNE)
print(INTERLIGNE)
print(INTERLIGNE)


