def solve(array):
    stack = []
    vector = []
    for i in range(len(array)-1, -1, -1):
        if len(stack) == 0:
            vector.append(-1)
        elif array[i] <= stack[-1]:
            vector.append(stack[-1])
        else:
            while len(stack) > 0 and array[i] > stack[-1]:
                stack.pop()
            if len(stack) > 0:
                vector.append(stack[-1])
            else:
                vector.append(-1)
        stack.append(array[i])
    return vector[::-1]


if __name__ == "__main__":
    array = [1, 0, 3, 5, 1, 2, 4]
    print(solve(array))