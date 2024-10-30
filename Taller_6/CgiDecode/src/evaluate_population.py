from typing import List

from src.get_fitness_cgi_decode import get_fitness_cgi_decode

def evaluate_population(population: List[List[str]]) -> dict:
    fitness = {}
    for ind in population:
        fit = get_fitness_cgi_decode(ind)
        fitness.update({ind: fit})
    return fitness
