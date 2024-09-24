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

    def gathering(self):
        '''
            aditionne (x,y)       à (distance)
            ajoute chaque fleurs  à [path]
        '''

        # Converti les éléments du dictionnaire en une liste
        flowers_list = list(flowers_dict.items())
        random.shuffle(flowers_list)


        for flower_id, (x,y) in flowers_list:
            #  NOT CORRECT, HAS TO TAKE NEGATIVE VALUES IN ACCOUNT
            self.distance = (self.distance[0] + abs(x), self.distance[1] + abs(y))
            # Add the flower's ID to [path]
            self.path.append(flower_id)
            # Add the flower's ID to [done]
            self.flowers_done.append(flower_id)
            

        while len(self.flowers_done) < len(flowers_dict):
            # Continue à butiner
            pass

        # Retourner à la ruche (500, 500) après avoir visité toutes les fleurs
        return "\nToutes les fleurs ont été butinées"



abeille = Abeille()
gahtering_1 = abeille.gathering()
print(gahtering_1)

print("\nTotal (x,y) de la distance parcourue:", abeille.distance)
print("\nListe des fleurs butinée :", abeille.path)