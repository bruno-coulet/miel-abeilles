from Bee import Bee

GENERATION = 100

def generate_100_bees() -> list:
    bees = []
    for i in range(GENERATION):
        bees.append(Bee())
    return bees

# bees = generate_100_bees()

def return_all_distances() -> list:
    distance_list = []
    for bee in generate_100_bees():
        distance_list.append(bee.gathering_distance())
    return distance_list

def sort_distance_list() -> list:
    distance_list = return_all_distances()
    distance_list.sort()
    return distance_list

def choose_best_bees(rate):
    distance_list = sort_distance_list()
    return distance_list[0:rate]
    

def return_all_paths() -> list:
    path_list = []
    for bee in generate_100_bees():
        path_list.append(bee.gathering_path())
    return path_list



# print(sort_distance_list())
print (choose_best_bees(20))