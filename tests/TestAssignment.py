import unittest
import os
from os import path

from components.Assignment import population, sort_values, sum_map


class TestAssignment(unittest.TestCase):

    def test_sort_valuese(self):
        expected = '''2 8 54
a v y'''
        actual = sort_values(2, 'a', 54, 'v', 'y', 8)
        self.assertEqual(expected, actual)

    def test_population(self):
        self.assertEqual(0, population(0))
        self.assertEqual(3, population(1))
        # two men
        # four woment
        # 8 children
        self.assertEqual(14, population(2))

    def _get_file_content(self):
        with open('summa.txt') as f:
            return f.readlines()

    def test_sum_map(self):
        if path.exists("summa.txt"):
            os.remove("summa.txt")
        self.assertEqual(29, sum_map(
            {"test": 22, "arveldus": 7, "tulevik": 112}))
        self.assertEqual(["29\n"], self._get_file_content())
        self.assertEqual(22, sum_map({"test": 22, "arveldu": 7, "uu": 112}))
        self.assertEqual(["29\n", "22\n"], self._get_file_content())


if __name__ == '__main__':
    unittest.main()
