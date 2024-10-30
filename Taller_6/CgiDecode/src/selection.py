from random import sample
from typing import List, Tuple


def selection(fitness_by_individual: dict, tournament_size: int) -> Tuple[List[str], float]:
    """
    fitness_by_individual: Diccionario que contiene a los individuos de la población como keys y su fitness como valores.
    tournament_size: Tamaño del torneo (entero positivo).
    """
    winner = None
    #  (Tournament selection)

    lista_tuplas = list(fitness_by_individual.items())
    selected = sample(lista_tuplas, tournament_size)

    winner = min(selected, key=lambda x: x[1])[0]

    return winner, fitness_by_individual[winner]
