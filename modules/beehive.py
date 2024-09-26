import random, math
from champs import champs, hive
from flowers_dict import flowers_dict 
# différentes classes et fonctions
# permettant le bon fonctionnement de l’évolution des abeilles

class Bee:
    def __init__(self, path):
        self._id = id
        # self._distance = 0                          deviens la ligne suivante
        # self._distance = self._compute_distance()   deviens la ligne suivante
        self._compute_distance()
        self._path = path
        # self.flowers_done = []
        # self.initial_position = (500,500)
        # self.hive = (500,500)

    def get_path(self):
        return self._path
    
    def _compute_distance(self) -> None:
        d = 5
        self._distance = d
        # self._path


class Beehive:
    def __init__(self):
        pass

    def select():
        pass

    def cross():
        pass

    def mutate():
        pass

    def reproduce():
        pass

def _compute_distance(self, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

def _compute_path_length(self) ->None:
    self._length = 0
    for i in range(len(self._path)-1):
        self._length += self._compute_distance(self._path[i], self._path[i+1])

def __str__(self) -> str:
    return f"The bee {self._id} has length {round(self._length,2)}"


# main.py
NUM_GENERATION = 100  
path = [(53,23), (16,34), (56,1), (53,23)]
for i in range(NUM_GENERATION):
    b = Bee(id,path)
print(b)
b._path

    # # def distance(x1, y1, x2, y2):
    # #     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # def gathering(self):
    #     '''
    #         aditionne (x,y)       à (distance)
    #         ajoute chaque fleurs  à [path]
    #     '''

    #     # Converti les éléments du dictionnaire en une liste
    #     flowers_list = list(flowers_dict.items())
    #     random.shuffle(flowers_list)


    #     for flower_id, (x,y) in flowers_list:
    #         #  NOT CORRECT, HAS TO TAKE NEGATIVE VALUES IN ACCOUNT
    #         self.distance = (self.distance[0] + abs(x), self.distance[1] + abs(y))
    #         # Add the flower's ID to [path]
    #         self.path.append(flower_id)
    #         # Add the flower's ID to [done]
    #         self.flowers_done.append(flower_id)
            

    #     while len(self.flowers_done) < len(flowers_dict):
    #         # Continue à butiner
    #         pass
    #     else:
    #         # Retourner à la ruche (500, 500) après avoir visité toutes les fleurs
    #         pass

    #     return "\nToutes les fleurs ont été butinées"



# abeille = Abeille()

# print(abeille.gathering())
# print("\nTotal (x,y) de la distance parcourue:", abeille.distance)
# print("\nListe des fleurs butinée :", abeille.path)