def josephus_problem(array, k, index):
    if len(array) == 1:
        print(array[0])
        return
    index = (index + k) % len(array)
    array.pop(index)
    josephus_problem(array, k, index)


if __name__ == "__main__":
    n = 5
    k = 2
    array = [i for i in range(1, n+1)]
    index = 0
    josephus_problem(array, k-1, index)