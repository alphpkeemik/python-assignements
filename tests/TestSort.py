import unittest

from components.Sort import sort_values


class TestIndependent(unittest.TestCase):

    def test_transform_age(self):
        expected = '''2 8 54
a v y'''
        actual = sort_values(2,'a',54,'v','y',8)
        self.assertEqual(expected, actual)
       


if __name__ == '__main__':
    unittest.main()
