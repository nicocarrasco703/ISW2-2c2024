#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode


class TestCgiDecode(unittest.TestCase):

    def testMas(self):
        t = cgi_decode("a+b")
        self.assertEqual("a b", t)

    def testPorciento(self):
        t = cgi_decode("%01")
        self.assertEqual("\x01",t)

    def testErrorLowDigit(self):
        self.assertRaisesRegex(ValueError, "Invalid encoding: digit low is not a hex digit", cgi_decode, "%fg")

    def testErrorHighDigit(self):
        self.assertRaisesRegex(ValueError, "Invalid encoding: digit high is not a hex digit", cgi_decode, "%gf")