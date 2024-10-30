import random
import string
from typing import List


def get_random_character():
    return random.choice(string.printable)


def create_test_case() -> str:
    n = random.choice(range(0, 11))
    res = ""
    for i in range(n):
        res = res + get_random_character()
    return res


def create_individual() -> List[str]:
    n = random.choice(range(1, 16))
    ind = []
    for i in range(n):
        ind.append(create_test_case())
    return ind


def create_population(population_size) -> List[List[str]]:
    population = []
    for i in range(population_size):
        population.append(create_individual())
    return population
