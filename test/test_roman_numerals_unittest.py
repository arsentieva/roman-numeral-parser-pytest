import unittest
from app.roman_numerals import parse

class TestRomanNumerals(unittest.TestCase):
    def test_i(self):
        value = parse("I")
        self.assertEqual(value, 1)

    def test__ii(self):
        value =parse("II")
        self.assertEqual(value, 2)
    def test__iii(self):
        value =parse("III")
        self.assertEqual(value, 3)
    def test__iv(self):
        value =parse("IV")
        self.assertEqual(value, 4)
    def test__v(self):
        value =parse("V")
        self.assertEqual(value, 5)
    def test__vi(self):
        value =parse("VI")
        self.assertEqual(value, 6)
    def test__vii(self):
        value =parse("VII")
        self.assertEqual(value, 7)
    def test__viii(self):
        value =parse("VIII")
        self.assertEqual(value, 8)
