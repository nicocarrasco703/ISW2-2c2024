from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:
    offspring1 = None
    offspring2 = None
    n1 = len(offspring1)
    n2 = len(offspring2)
    offspring1_half1 = offspring1[:(n1/2)]
    offspring1_half2 = offspring1[(n1 / 2):]
    offspring2_half1 = offspring2[:(n2 / 2)]
    offspring2_half2 = offspring2[(n2 / 2):]
    offspring1 = offspring1_half1 + offspring2_half2
    offspring2 = offspring2_half1 + offspring1_half2
    return offspring1, offspring2
