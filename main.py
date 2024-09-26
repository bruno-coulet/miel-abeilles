from bee import Bee

GENERATION = 100
CHOSEN_BEES = 10

def generate_bees() -> list:
    bees = []
    for i in range(GENERATION):
        bees.append(Bee())
    return bees

def distances_and_bees() -> list [float, object]:
    distances_and_bees = []
    for bee in generate_bees():
        distances_and_bees.append((bee.gathering_distance(), bee))
    return distances_and_bees
# print(distances_and_bees())


def sort_distance_list() -> list:
    sorted_distances_list = distances_and_bees()
    sorted_distances_list.sort()
    return sorted_distances_list
print(sort_distance_list())

def best_bees(CHOSEN_BEES):
    best_bees = sort_distance_list()
    return best_bees[0:CHOSEN_BEES]
    

def return_paths() -> list:
    path_list = []
    for bee in generate_bees():
        path_list.append(bee.gathering_path())
    return path_list


# def best_paths(CHOSEN_BEES):
#     best_path_list = []
#     for bee in best_bees(CHOSEN_BEES):
#         best_path_list.append(path_list(best_bees))
 
#     return best_path_list





print (f'\nLes {CHOSEN_BEES} meilleurs temps de parcours sont :\n {best_bees(CHOSEN_BEES)}')

# print(sort_distance_list())

# print (return_paths())
# print(best_paths(CHOSEN_BEES))
