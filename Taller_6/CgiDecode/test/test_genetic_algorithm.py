#!./venv/bin/python
import unittest

from random import seed
from src.genetic_algorithm import GeneticAlgorithm


class TestGeneticAlgorithm(unittest.TestCase):
    def test1(self):
        seed(912)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.generation, 130)
        self.assertEqual(ga.fitness_best_individual, 0.0)

    def test2(self):
        seed(8)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.generation, 1)
        self.assertEqual(ga.fitness_best_individual, 0.0)

    def test3(self):
        seed(666)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.generation, 278)
        self.assertEqual(ga.fitness_best_individual, 0.0)