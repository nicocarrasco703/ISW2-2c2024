#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, get_true_distance, get_false_distance


class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):

    def testMas(self):
        clear_maps()
        self.assertEqual("Hello World", cgi_decode_instrumented("Hello+World"))
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_true_distance(2), 0)
        self.assertEqual(get_true_distance(3), 35)
        self.assertEqual(get_false_distance(1), 0)
        self.assertEqual(get_false_distance(2), 0)
        self.assertEqual(get_false_distance(3), 0)


    def testPorciento(self):
        clear_maps()
        t = cgi_decode_instrumented("%01")
        self.assertEqual("\x01",t)
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_true_distance(2), 6)
        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_true_distance(4), 0)
        self.assertEqual(get_true_distance(5), 0)
        self.assertEqual(get_false_distance(1), 0)
        self.assertEqual(get_false_distance(2), 0)
        self.assertEqual(get_false_distance(3), 1)
        self.assertEqual(get_false_distance(4), 1)
        self.assertEqual(get_false_distance(5), 1)

    def testErrorLowDigit(self):
        clear_maps()
        self.assertRaisesRegex(ValueError, "Invalid encoding: digit low is not a hex digit", cgi_decode_instrumented, "%fg")
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_true_distance(2), 6)
        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_true_distance(4), 0)
        self.assertEqual(get_true_distance(5), 1)
        self.assertEqual(get_false_distance(1), 3)
        self.assertEqual(get_false_distance(2), 0)
        self.assertEqual(get_false_distance(3), 1)
        self.assertEqual(get_false_distance(4), 1)
        self.assertEqual(get_false_distance(5), 0)

    def testErrorHighDigit(self):
        clear_maps()
        self.assertRaisesRegex(ValueError, "Invalid encoding: digit high is not a hex digit", cgi_decode_instrumented, "%gf")
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_true_distance(2), 6)
        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_true_distance(4), 1)
        self.assertEqual(get_false_distance(1), 3)
        self.assertEqual(get_false_distance(2), 0)
        self.assertEqual(get_false_distance(3), 1)
        self.assertEqual(get_false_distance(4), 0)