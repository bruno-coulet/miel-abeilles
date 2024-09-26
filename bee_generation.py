from Bee import Bee

GENERATION = 100
CHOSEN_BEES = 20

def generate_100_bees() -> list:
    bees = []
    for i in range(GENERATION):
        bees.append(Bee())
    return bees


def distances_list() -> list:
    distances_list = []
    for bee in generate_100_bees():
        distances_list.append(bee.gathering_distance())
    return distances_list

def sort_distance_list() -> list:
    sorted_distances_list = distances_list()
    sorted_distances_list.sort()
    return sorted_distances_list

def best_bees(CHOSEN_BEES):
    # distance_list = sort_distance_list()
    # return distance_list[0:BEST_BEES]
    best_bees = sort_distance_list()
    return best_bees[0:CHOSEN_BEES]
    

def return_all_paths() -> list:
    path_list = []
    for bee in generate_100_bees():
        path_list.append(bee.gathering_path())
    return path_list

def best_paths(CHOSEN_BEES):
    pass


# print(sort_distance_list())
print (f'\nLes {CHOSEN_BEES} meilleurs temps de parcours sont : {best_bees(CHOSEN_BEES)}')
# print (return_all_paths())