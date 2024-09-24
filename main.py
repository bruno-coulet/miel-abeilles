
import random, math
from modules.champs import *
from modules.champs import champs, hive
from modules.flowers_dict import flowers_dict 
#  simulation de l'adaptation des abeilles.

path=[]
hive = (500,500)


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



def gathering_distance():
    
    distance = (0,0)
    for flowers in shuffle_flowers_list():
        #  NOT CORRECT, HAS TO TAKE NEGATIVE VALUES IN ACCOUNT
        distance = (distance[0] + x, distance[1] + y)
    return distance


''' Add the flowers ID to [path]'''
def gathering_path():
    for flower in shuffle_flowers_list():
        path.append(flower)
    return f"\nToutes les fleurs ont été butinées {path}"


# shuffle_flowers_list()
print (gathering_distance())
print("\nTotal (x,y) de la distance parcourue:", gathering_distance())
print("\nListe des fleurs butinée :", gathering_path())