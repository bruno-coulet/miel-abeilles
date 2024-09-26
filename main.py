from bee import Bee

GENERATION = 10
CHOSEN_BEES = 3

generated_bees = []

def generate_bees() -> list:
    global generated_bees
    if generated_bees != []:
        return generated_bees
    else:
        for i in range(GENERATION):
            generated_bees.append(Bee(i))
    return generated_bees

def distances_and_bees() -> list [float, int]:
    distances_and_bees = []
    for bee in generate_bees():
        distances_and_bees.append((bee.gathering_distance(), bee))
        # distances_and_bees.append((bee.gathering_distance(), bee.bee_id))
        # distances_and_bees.append((bee.gathering_distance(), bee.bee_path))
    return distances_and_bees
# print(distances_and_bees())


def sort_distance_list() -> list:
    sorted_distances_list = distances_and_bees()
    # Tri par distance
    sorted_distances_list.sort(key=lambda x: x[0])
    return sorted_distances_list
# print(sort_distance_list())

def best_bees(CHOSEN_BEES):
    best_bees = sort_distance_list()
    return best_bees[0:CHOSEN_BEES]


def paths() -> list:
    path_list = []
    for bee in generate_bees():
        path_list.append(bee.gathering_path())
    return path_list

def best_paths(CHOSEN_BEES):
    best_path_list = []
    # ajout pour récupérer les chemins
    best_bees_data = best_bees(CHOSEN_BEES)
    for distance, bee in best_bees_data:
        best_path_list.append(bee.gathering_path())
    # for bee in best_bees(CHOSEN_BEES):
       # best_path_list.append(best_path_list(best_bees))
    return best_path_list



print(f"\nLes {CHOSEN_BEES} meilleurs temps de parcours, et les abeilles correspondantes sont :\n{[(bee.bee_id, distance) for distance, bee in best_bees(CHOSEN_BEES)]}")
print (f"\nles meilleurs chemins sont : {best_paths(CHOSEN_BEES)}")


# print (f"\nLes {CHOSEN_BEES} meilleurs temps de parcours, et les numéros des abeilles sont :\n {best_bees(CHOSEN_BEES)}")
# print (f"les meilleurs chemins sont : {best_paths(CHOSEN_BEES)}")
# print(sort_distance_list())

# print (paths())
# print(best_paths(CHOSEN_BEES))
