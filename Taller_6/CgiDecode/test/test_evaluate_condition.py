#!./venv/bin/python
import unittest
from src.evaluate_condition import evaluate_condition


class TestEvaluateCondition(unittest.TestCase):

    def test_evaluate_condition_eq_int(self):
        # Probar igualdad de enteros
        self.assertTrue(evaluate_condition(1, "Eq", 5, 5))
        self.assertFalse(evaluate_condition(1, "Eq", 5, 3))

    def test_evaluate_condition_ne_int(self):
        # Probar desigualdad de enteros
        self.assertTrue(evaluate_condition(1, "Ne", 5, 3))
        self.assertFalse(evaluate_condition(1, "Ne", 5, 5))

    def test_evaluate_condition_lt_int(self):
        # Probar menor que con enteros
        self.assertTrue(evaluate_condition(1, "Lt", 3, 5))
        self.assertFalse(evaluate_condition(1, "Lt", 5, 3))

    def test_evaluate_condition_gt_int(self):
        # Probar mayor que con enteros
        self.assertTrue(evaluate_condition(1, "Gt", 5, 3))
        self.assertFalse(evaluate_condition(1, "Gt", 3, 5))

    def test_evaluate_condition_le_int(self):
        # Probar menor o igual que con enteros
        self.assertTrue(evaluate_condition(1, "Le", 5, 5))
        self.assertTrue(evaluate_condition(1, "Le", 3, 5))
        self.assertFalse(evaluate_condition(1, "Le", 5, 3))

    def test_evaluate_condition_ge_int(self):
        # Probar mayor o igual que con enteros
        self.assertTrue(evaluate_condition(1, "Ge", 5, 5))
        self.assertTrue(evaluate_condition(1, "Ge", 5, 3))
        self.assertFalse(evaluate_condition(1, "Ge", 3, 5))

    def test_evaluate_condition_eq_str(self):
        # Probar igualdad de caracteres
        self.assertTrue(evaluate_condition(1, "Eq", 'a', 'a'))
        self.assertFalse(evaluate_condition(1, "Eq", 'a', 'b'))

    def test_evaluate_condition_ne_str(self):
        # Probar desigualdad de caracteres
        self.assertTrue(evaluate_condition(1, "Ne", 'a', 'b'))
        self.assertFalse(evaluate_condition(1, "Ne", 'a', 'a'))

    def test_evaluate_condition_lt_str(self):
        # Probar menor que con caracteres
        self.assertTrue(evaluate_condition(1, "Lt", 'a', 'b'))
        self.assertFalse(evaluate_condition(1, "Lt", 'b', 'a'))

    def test_evaluate_condition_gt_str(self):
        # Probar mayor que con caracteres
        self.assertTrue(evaluate_condition(1, "Gt", 'b', 'a'))
        self.assertFalse(evaluate_condition(1, "Gt", 'a', 'b'))

    def test_evaluate_condition_le_str(self):
        # Probar menor o igual que con caracteres
        self.assertTrue(evaluate_condition(1, "Le", 'a', 'a'))
        self.assertTrue(evaluate_condition(1, "Le", 'a', 'b'))
        self.assertFalse(evaluate_condition(1, "Le", 'b', 'a'))

    def test_evaluate_condition_ge_str(self):
        # Probar mayor o igual que con caracteres
        self.assertTrue(evaluate_condition(1, "Ge", 'a', 'a'))
        self.assertTrue(evaluate_condition(1, "Ge", 'b', 'a'))
        self.assertFalse(evaluate_condition(1, "Ge", 'a', 'b'))

    def test_evaluate_condition_in_str_dict(self):
        # Probar la operación "In" con un diccionario y un carácter
        self.assertTrue(evaluate_condition(1, "In", 'a', {ord('a'): 1, ord('b'): 2}))
        self.assertFalse(evaluate_condition(1, "In", 'c', {ord('a'): 1, ord('b'): 2}))

    def test_evaluate_error_int(self):
        self.assertRaises(ValueError, evaluate_condition, 1, "InvalidOp", 5, 5)

    def test_evaluate_error_str(self):
        self.assertRaises(ValueError, evaluate_condition, 1, "InvalidOp", 'a', 'b')

    def test_evaluate_error_in_str_dict(self):
        self.assertRaises(ValueError, evaluate_condition, 1, "InvalidOp", 'a', {ord('a'): 1, ord('b'): 2})

    def test_evaluate_error(self):
        self.assertRaises(ValueError, evaluate_condition, 1, "InvalidOp", 5, 'a')
