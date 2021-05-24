def sort_using_recursion(array):
    if len(array) == 1:
        return array
    n = array.pop()
    sort_using_recursion(array)
    return insert(array, n)


def insert(array, temp):
    if len(array) == 0 or array[len(array) - 1] <= temp:
        array.append(temp)
        return array
    n = array.pop()
    insert(array, temp)
    array.append(n)
    return array


if __name__ == "__main__":
    array = [5, 1, 6, 7, 1, 3]
    print(sort_using_recursion(array))