from random import random
from typing import List

from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_population import evaluate_population
from src.mutate import mutate
from src.selection import selection

class GeneticAlgorithm():
    def __init__(self):
        self.population_size = 100
        self.tournament_size = 5
        self.p_crossover = 0.70
        self.p_mutation = 0.20

        self.generation = 0
        self.best_individual = None
        self.fitness_best_individual = None

    def get_best_individual(self):
        return self.best_individual
    
    def get_fitness_best_individual(self):
        return self.fitness_best_individual
    
    def get_generation(self):
        return self.generation

    def generate_crossovers(self, population: List[List[str]], fitness_by_individual: dict) -> List[List[str]]:
        # Pista: no olvidarse de usar selection, deben crear una nueva poblacion
        p1 = selection(fitness_by_individual, self.tournament_size)
        p2 = selection(fitness_by_individual, self.tournament_size)
        if random() < self.p_crossover:
            c = crossover(p1[0], p2[0])
            population.append(c[0])
            population.append(c[1])
        else:
            population.append(p1[0])
            population.append(p2[0])
        return population

    def generate_mutations(self, population: List[List[str]]) -> List[List[str]]:
        i = len(population) - 2
        if random() < self.p_mutation:
            population[i] = mutate(population[i])
        if random() < self.p_mutation:
            population[i+1] = mutate(population[i+1])
        return population

    def covered_all_branches(self, fitness_individual: float) -> bool:
        return fitness_individual < 1e-05

    def run(self):
        # Generar y evaluar la poblacion inicial
        population = create_population(self.population_size)
        fitness_by_individual = evaluate_population(population)

        # Imprimir el mejor valor de fitness encontrado
        self.best_individual = min(fitness_by_individual, key = lambda k: fitness_by_individual.get(k))
        self.fitness_best_individual = fitness_by_individual.get(tuple(self.best_individual))
        print(self.fitness_best_individual)

        # Continuar mientras la cantidad de generaciones es menor que 1000
        # y no haya ningun individuo que cubra todos los objetivos

        while self.generation < 1000 and all(not self.covered_all_branches(fitness_by_individual.get(tuple(ind))) for ind in population):

            new_population = []
            while len(new_population) < self.population_size:
                # Producir una nueva poblacion en base a la anterior.
                # Usar selection, crossover y mutation.
                new_population = self.generate_crossovers(new_population, fitness_by_individual)
                new_population = self.generate_mutations(new_population)

            # Una vez creada, reemplazar la poblacion anterior con la nueva
            self.generation += 1
            population = new_population

            # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
            fitness_by_individual = evaluate_population(population)
            self.best_individual = min(fitness_by_individual, key=lambda k: fitness_by_individual.get(k))
            self.fitness_best_individual = fitness_by_individual.get(tuple(self.best_individual))
            print(self.fitness_best_individual)

        # retornar el mejor individuo de la ultima generacion
        print(self.generation)
        print(self.fitness_best_individual)
        return self.best_individual