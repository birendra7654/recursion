import unittest

def flatten_array(array):
    res = []
    for i in array:
        if isinstance(i, list):
            res.extend(flatten_array(i))
        else:
            res.append(i)
    return res


class FlattenTest(unittest.TestCase):
    def test_flattern_array(self):
        array = [[1], [2, 3], [4], [3, [2, 4]]]
        actual = [1, 2, 3, 4, 3, 2, 4]
        expected = flatten_array(array)
        for i, j in zip(actual, expected):
            self.assertEqual(i, j)

    def test_nested_array(self):
        """ This tests on a live database :( """
        array = [[[[1, 2], 3]]]
        actual = [1, 2, 3]
        expected = flatten_array(array)
        for i, j in zip(actual, expected):
            self.assertEqual(i, j)


if __name__ == "__main__":
    unittest.main()