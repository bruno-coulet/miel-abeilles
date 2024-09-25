
import random, math
#  simulation de l'adaptation des abeilles.

def shuffle_flowers_list():
    flowers_list = [
    (796, 310),
    (774, 130),
    (116, 69),
    (908, 534),
    (708, 99),
    (444, 428),
    (220, 307),
    (501, 287),
    (345, 560),
    (628, 311),
    (901, 639),
    (436, 619),
    (938, 646),
    (45, 549),
    (837, 787),
    (328, 489),
    (278, 434),
    (704, 995),
    (101, 482),
    (921, 964),
    (493, 970),
    (494, 898),
    (929, 389),
    (730, 742),
    (528, 794),
    (371, 429),
    (98, 711),
    (724, 631),
    (573, 903),
    (964, 726),
    (213, 639),
    (549, 329),
    (684, 273),
    (273, 105),
    (897, 324),
    (508, 31),
    (758, 405),
    (862, 361),
    (898, 898),
    (2, 897),
    (951, 209),
    (189, 739),
    (602, 68),
    (437, 601),
    (330, 410),
    (3, 517),
    (643, 404),
    (875, 407),
    (761, 772),
    (276, 666)
]
    random.shuffle(flowers_list)
    return flowers_list

random_flowers_list = shuffle_flowers_list()

def distance_a_to_b(a,b):
    """Calculates the Euclidean distance between two points."""
    stage_distance = round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2),2)
    return stage_distance

def gathering_distance():
    """Calculates the total distance from the hive, through every shuffled flower,back to the hive."""
    hive = (500, 500)
    current_position = hive
    # flowers_list = shuffle_flowers_list()
    total_distance = 0

    for flower in random_flowers_list:
        stage_distance = distance_a_to_b(current_position, flower)
        total_distance += stage_distance
        current_position = flower
    
    return_to_hive_distance = distance_a_to_b(current_position, hive)
    total_distance += return_to_hive_distance
    total_distance = round(total_distance,2)
        
    print(f"\n'gathering_distance'-> Distance totale parcourue : {total_distance}")
    return total_distance

def gathering_path():
    ''' Add the flowers ID to [path]'''
    path=[]
    for flower in random_flowers_list:
        path.append(flower)
    print(f"\n'gathering_path' -> Les fleurs ont été butinées dans cet ordre : {path}")
    return path



distance = gathering_distance()
path = gathering_path()
