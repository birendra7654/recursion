import unittest
from typing import List


def capitalize_word(array: List[str]):
    if len(array) == 0:
        return []
    for i in range(len(array)):
        return [array[i].upper()] + capitalize_word(array[i+1:])


class FlattenTest(unittest.TestCase):
    def test_capitalize_array(self):
        array = ['Foo']
        expected = ['FOO']
        actual = capitalize_word(array)
        for i, j in zip(actual, expected):
            self.assertEqual(i, j)

    def test_nested_array(self):
        """ This tests on a live database :( """
        array = ['foo', 'bar', 'world', 'hello']
        expected = ['FOO', 'BAR', 'WORLD', 'HELLO']
        actual = capitalize_word(array)
        for i, j in zip(actual, expected):
            self.assertEqual(i, j)


if __name__ == "__main__":
    unittest.main()