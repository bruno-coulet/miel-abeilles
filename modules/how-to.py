path = [(53,23), (16,34), (56,1), (53,23)]

class Bee:
    def __init__(self, bee_id, path):
        self._id = bee_id
        # self._distance = 0
        # remplacé par la ligne suivante
        # self._distance = self._compute_distance()
        # remplacé par la ligne suivante
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

    def _compute_distance(self, a, b) -> float :
        """Computes the Euclidean distance between two points a and b."""
        x1, y1 = a
        x2, y2 = b
        return round((((b[0] - a[0])**2 + (b[1] - a[1])**2)**0,5),2)

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
    bee = Bee(id, path)
print(bee)
print(bee._path)