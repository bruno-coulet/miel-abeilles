from bee import Bee

POPULATION = 5
SELECTION = 2

generated_bees = []

def generate_bees() -> list:
    ''' generates as many bees as defined in POPULATION '''
    # Doesn't create a new list of bees if there is one already
    if generated_bees != []:
        return generated_bees
    # Creates a list of bees if there is none
    else:
        for i in range(POPULATION):
            generated_bees.append(Bee(i))
    return generated_bees
print(generate_bees())

def distances_and_bees() -> list [float, int]:
    ''' processes the distance each bee travels '''
    distances_and_bees = []
    for bee in generate_bees():
        distances_and_bees.append((bee.total_distance(), bee))
    return distances_and_bees
# print(distances_and_bees())

def sort_distance_list() -> list:
    ''' sorts the distances_and_bees list
    shortest distance first, longest distance last'''
    sorted_distances_list = distances_and_bees()
    sorted_distances_list.sort()
    return sorted_distances_list
# print(sort_distance_list())

def selected_bees(SELECTION) -> list:
    ''' slices the distances_and_bees list according to SELECTION '''
    selected_bees = sort_distance_list()
    return selected_bees[0:SELECTION]

def best_paths(SELECTION) -> list:
    ''' lists the paths of the best bees '''
    best_paths = []
    chosen_bees = selected_bees(SELECTION)
    for distance, bee in chosen_bees:
        best_paths.append((bee.gathering_path(), bee.bee_id))
    return best_paths


print()
print("Population : ",POPULATION," abeilles")
print()
print("Selection : ",SELECTION," abeilles")
print()


print(f"\nLes {SELECTION} meilleures abeilles et leurs distances :\n")
for distance, bee in selected_bees(SELECTION):
    print(f"Abeille {bee.bee_id} avec une distance de {distance}")
print()
# print(f"\nLes {SELECTION} meilleurs abeilles et leur distances :\n{[(bee.bee_id, distance) for distance, bee in selected_bees(SELECTION)]}")


# best paths
print(f"Chemins des {SELECTION} meilleures abeilles :\n\n {best_paths(SELECTION)}\n")

