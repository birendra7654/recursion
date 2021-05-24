import unittest
from typing import List


def is_even(num: int) -> bool:
    if num & 1:
        return False
    return True


def any_even(array: List[int], cb):
    if len(array) == 0:
        return False
    if cb(array[0]):
        return True
    return any_even(array[1:], cb)


class FlattenTest(unittest.TestCase):
    def test_mixed_of_even_odd(self):
        array = [1, 2, 3, 4, 5]
        actual = any_even(array, is_even)
        print(actual)
        self.assertTrue(actual)

    def test_all_even(self):
        """ This tests on a live database :( """
        array = [2, 4, 6]
        actual = any_even(array, is_even)
        self.assertTrue(actual)

    def test_all_odd(self):
        """ This tests on a live database :( """
        array = [1, 3, 5]
        actual = any_even(array, is_even)
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()