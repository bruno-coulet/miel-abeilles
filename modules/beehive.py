import random
from champs import champs, hive
from flowers_dict import flowers_dict 
# différentes classes et fonctions
# permettant le bon fonctionnement de l’évolution des abeilles

class Abeille:

    def __init__(self):
        self.distance = (0,0)
        self.path=[]
        self.flowers_done = []
        self.initial_position = (500,500)
        self.hive = (500,500)

    def gathering(self, flowers_dict,):
        '''
            aditionne (x,y)       à (distance)
            ajoute chaque fleurs  à [path]
        '''
        for flower_id, (x,y) in flowers_dict.items():

            # Update the distance by adding the flower's coordinates
            #  NOT CORRECT, HAS TO TAKE NEGATIVE VALUES IN ACCOUNT
            self.distance = (self.distance[0] + abs(x), self.distance[1] + abs(y))
            # Add the flower's ID to [path]
            self.path.append(flower_id)
            # Add the flower's ID to [done]
            self.flowers_done.append(flower_id)
            

        while sum(self.flowers_done) != 1275:
            # continue à butiner
            pass

        else:
            # retourne à hive (500,500)
            pass



abeille = Abeille()
final_position = abeille.gathering(flowers_dict)
print("Final position:", final_position)

print("Total de la distance parcourue:", abeille.distance)
print("Fleurs butinée :", abeille.path)