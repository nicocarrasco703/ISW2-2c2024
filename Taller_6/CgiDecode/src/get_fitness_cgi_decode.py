from typing import List

from src.cgi_decode import cgi_decode
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, distances_true, distances_false


def get_fitness_cgi_decode(test_suite: List[str]) -> float:
    # Borro la información de branch coverage de ejecuciones anteriores
    # Recuerden que los diccionarios true_distances y false_distances son globales

    fitness = 0
    clear_maps()

    for test in test_suite:
        try:
            cgi_decode_instrumented(test)
        except:
            pass
    for i in range(1,6):
        if i in distances_true.keys():
            fitness += distances_true[i] / (distances_true[i]+1)
            fitness += distances_false[i] / (distances_false[i]+1)
        else:
            fitness += 2

    return fitness
