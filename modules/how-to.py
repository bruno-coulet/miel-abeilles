path = [(53,23), (16,34), (56,1), (53,23)]

class Bee:

    def __init__(self, path):
        # self._distance = 0
        # remplacé par la ligne suivante
        # self._distance = self._compute_distance()
        # remplacé par la ligne suivante
        self._id = id
        self._compute_distance()
        self._path = path
        self.flowers_done = []
        self.initial_position = (500,500)
        self.hive = (500,500)

    def generate_random_bees() -> list:
        bees = []
        for i in range(GENERATION):
            bees.append(Bee(i))
        return bees

    def get_path(self):
        return self._path
    
    # def _compute_distance(self) -> None:
    #     d = 5
    #     self._distance = d
    #     # self._path

    def _compute_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

    def _compute_path_length(self) ->None:
        self._length = 0
        for i in range(len(self._path)-1):
            self._length += self._compute_distance(self._path[i], self._path[i+1])


class Beehive:

    def __init__(self):
        pass

    # def _compute_distance(self, p1, p2):
    #     x1, y1 = p1
    #     x2, y2 = p2

    def select():
        pass

    def cross():
        pass

    def mutate():
        pass

    def reproduce():
        pass



if __name__ == "__main__":
    pass

GENERATION = 100

def should_continue(bees):
    return True


bees = Bee.generate_random_bees()
print (len(bees))

while should_continue(bees):
    Beehive.select()
    Beehive.cross()
    Beehive.mutate() # parmis les meilleur trajets mettre la derniere fleur en 1er
    Beehive.reproduce()
