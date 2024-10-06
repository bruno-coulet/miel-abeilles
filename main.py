from beehive import Beehive
from constants import POPULATION_SIZE, SELECTION_RATE, CYCLE_NUMBER
import matplotlib.pyplot as plt


def main():
    # Générer la ruche avec la population d'abeilles initiale
    beehive = Beehive(POPULATION_SIZE)

    # Stocker les distances moyennes et les meilleures distances de chaque génération
    average_distances = []
    best_distances = []

    # Afficher la population initiale et les paramètres de sélection
    print(f"\nPopulation : {POPULATION_SIZE} abeilles\nTaux de sélection  : {SELECTION_RATE}\n")

    # Sélectionner les meilleures abeilles de la ruche
    beehive.select_bees()

    # Calculer et stocker la distance moyenne et la meilleure distance avant le croisement
    print("\nPerformances avant le croisement:")
    average_distance = beehive.average_distance()
    average_distances.append(average_distance)
    best_bee = beehive.bees[0]
    best_distances.append(best_bee.distance)
    print(f"Meilleure distance avant croisement : {best_bee.distance}, Distance moyenne : {average_distance}")

    print("\nDÉBUT DU CROSS OVER :\n")

    # Boucle pour effectuer les cycles de croisement et de mutation sur plusieurs générations
    for cycle in range(CYCLE_NUMBER):
        print(f"--- Génération {cycle + 1} ---")

        # Croisement des abeilles sélectionnées
        beehive.cross_bees()

        # Mutation des abeilles après croisement
        # Si tu souhaites utiliser une mutation, ajoute la méthode correspondante ici
        # beehive.mutate_first_to_last(beehive.bees)

        # Sélectionner de nouveau les meilleures abeilles après croisement/mutation
        beehive.select_bees()

        # Calculer et stocker la distance moyenne et la meilleure distance après le croisement
        average_distance = beehive.average_distance()
        average_distances.append(average_distance)
        best_bee = beehive.bees[0]  # La meilleure abeille est toujours la première après tri
        best_distances.append(best_bee.distance)
        print(f"Meilleure distance après croisement : {best_bee.distance}, Distance moyenne : {average_distance}")

    # Afficher la meilleure solution trouvée
    print(f"\nMeilleure solution trouvée : {best_bee.path}, Distance : {best_bee.distance}")

    # Tracer le graphe de l'évolution des distances moyennes et des meilleures distances
    plt.plot(range(CYCLE_NUMBER + 1), average_distances, marker='o', linestyle='-', color='b', label='Distance moyenne')
    plt.plot(range(CYCLE_NUMBER + 1), best_distances, marker='x', linestyle='--', color='r', label='Meilleure distance')

    # Titre et légendes du graphe
    plt.title('Évolution des performances de l\'essaim')
    plt.xlabel('Génération')
    plt.ylabel('Distance')
    
    # Ajouter une légende pour identifier les courbes
    plt.legend()

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
