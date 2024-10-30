#!./venv/bin/python
import unittest
from src.get_fitness_cgi_decode import get_fitness_cgi_decode


class TestGetFitnessCgiDecode(unittest.TestCase):

    def test01(self):
        self.assertEqual(get_fitness_cgi_decode(["%AA"]), 2.357142857142857)

    def test02(self):
        self.assertEqual(get_fitness_cgi_decode(["\%AA"]), 1.8571428571428572)

    def test03(self):
        self.assertEqual(get_fitness_cgi_decode(["\%AU"]) , 3.03021978021978)

    def test04(self):
        self.assertEqual(get_fitness_cgi_decode(["\%UU"]) , 4.53021978021978)

    def test05(self):
        self.assertEqual(get_fitness_cgi_decode(["Hello+Reader"]) , 4.972222222222222)

    def test06(self):
        self.assertEqual(get_fitness_cgi_decode([""]) , 8.5)

    def test07(self):
        self.assertEqual(get_fitness_cgi_decode(["\%"]) , 5.357142857142858)

    def test08(self):
        self.assertEqual(get_fitness_cgi_decode(["\%1"]) , 5.523809523809524)

    def test09(self):
        self.assertEqual(get_fitness_cgi_decode(["+"]) , 6.5)

    def test10(self):
        self.assertEqual(get_fitness_cgi_decode(["+\%1"]) , 4.666666666666666)

    def test11(self):
        self.assertEqual(get_fitness_cgi_decode(["\%1+"]) , 2.9404761904761907)

    def test12(self):
        self.assertEqual(get_fitness_cgi_decode(["\%1+", "%+1", "a+%AA"]) , 0)