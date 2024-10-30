from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:
    n1 = len(parent1)
    n2 = len(parent2)
    offspring1_half1 = parent1[:(n1//2)]
    offspring1_half2 = parent1[(n1//2):]
    offspring2_half1 = parent2[:(n2//2)]
    offspring2_half2 = parent2[(n2//2):]
    offspring1 = offspring1_half1 + offspring2_half2
    offspring2 = offspring2_half1 + offspring1_half2
    return offspring1, offspring2
