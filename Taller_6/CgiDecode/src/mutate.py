from random import choice, random
from typing import List

from src.create_population import create_test_case, get_random_character


def add_character(test_case: str) -> str:
    test_case + get_random_character()
    return test_case


def remove_character(test_case: str) -> str:
    i = choice(range(len(test_case)))
    return test_case[:i] + test_case[i+1:]


def modify_character(test_case: str) -> str:
    i = choice(range(len(test_case)))
    return test_case[:i] + get_random_character() + test_case[i + 1:]


def add_test_case(individual: List[str]) -> List[str]:
    individual.append(create_test_case())
    return individual


def remove_test_case(individual: List[str]) -> List[str]:
    i = choice(range(len(individual)))
    individual.pop(i)
    return individual


def modify_test_case(individual: List[str]) -> List[str]:
    i = choice(range(len(individual)))
    if 10 > len(individual[i]) > 1:
        j = choice(range(3))
    elif len(individual[i]) == 1:
        j = choice(range(2))
    elif len(individual[i]) == 0:
        j = 0
    else:
        j = choice(range(1,3))

    if j == 0:
        individual[i] = add_character(individual[i])
    if j == 1:
        individual[i] = modify_character(individual[i])
    if j == 2:
        individual[i] = remove_character(individual[i])
    return individual


def mutate(individual: List[str]) -> List[str]:
    if 15 > len(individual) > 1:
        j = choice(range(3))
    elif len(individual) == 1:
        j = choice(range(2))
    else:
        j = choice(range(1,3))

    if j == 0:
        individual = add_test_case(individual)
    if j == 1:
        individual = modify_test_case(individual)
    if j == 2:
        individual = remove_test_case(individual)
    return individual

