from Bee import Bee

GENERATION = 100

def generate_100_bees() -> list:
    bees = []
    for i in range(GENERATION):
        bees.append(Bee())
    return bees

bees = generate_100_bees()

for bee in bees:
    print(bee.one_bee_gathers())