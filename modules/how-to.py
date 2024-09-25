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

def _compute_distance(self, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

def _compute_path_length(self) ->None:
    self._length = 0
    for i in range(len(self._path)-1):
        self._length += _compute_distance(self._path[i], self._path[i])

