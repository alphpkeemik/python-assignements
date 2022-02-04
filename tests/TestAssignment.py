import unittest

from components.Assignment import population, sort_values


class TestAssignment(unittest.TestCase):

    def test_sort_valuese(self):
        expected = '''2 8 54
a v y'''
        actual = sort_values(2,'a',54,'v','y',8)
        self.assertEqual(expected, actual)
       

    def test_population(self):
        self.assertEqual(0, population(0))
        self.assertEqual(3, population(1))
        # two men
        # four woment
        # 8 children
        self.assertEqual(14, population(2))
       


if __name__ == '__main__':
    unittest.main()
