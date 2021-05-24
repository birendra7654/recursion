import unittest
from typing import List


def is_even(num: int) -> bool:
    if num & 1:
        return False
    return True


def even_sum(data):
    summation = 0
    for i in data:
        if isinstance(data[i], dict):
            summation += even_sum(data[i])
        else:
            if isinstance(data[i], int) and not ( data[i] & 1):
                summation += data[i]
    return summation


class EvenSumArrayTest(unittest.TestCase):
    def test_normal(self):
        data = {"a": 1, "b": 2}
        expected = 2
        actual = even_sum(data)
        self.assertEqual(actual, expected)

    def test_nested_dict(self):
        """ This tests on a live database :( """
        obj = {
            "a": 2,
            "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
            "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
            "d": 1,
            "e": {"nn": {"lil": 2}, "mm": 12}
        }
        actual = even_sum(obj)
        expected = 22
        self.assertEqual(actual, expected)

    def test_all_odd(self):
        """ This tests on a live database :( """
        data = {"a": 1, "c": {"b": 0 }}
        actual = even_sum(data)
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()