# For n = 5, the following combinations are possible:
#
# {5}
# {1, 4}
# {2, 3}
# {1, 1, 3}
# {1, 2, 2}
# {1, 1, 1, 2}
# {1, 1, 1, 1, 1}

def solve(arr, start, n, target):
    if sum(arr) == target:
        print(arr)
        return
    if sum(arr) > target:
        return

    for i in range(start, n):
        arr.append(i)
        solve(arr, i, n, target)
        arr.pop()


if __name__ == "__main__":
    n = 5
    start = 1
    arr = []
    target = n
    solve(arr, start, n+1, target)

