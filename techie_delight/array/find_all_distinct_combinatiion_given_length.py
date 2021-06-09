# Find all distinct combinations of a given length – II using knapsack 0/1

def solve(array, k, out, start, n):
    if k == 0:
        print(out)
        return
    if start == n:
        return
    out.append(array[start])
    solve(array, k-1, out, start+1, n)
    out.pop()
    while start < n-1 and array[start] == start+1:
        start += 1
    solve(array, k, out, start+1, n)


if __name__ == "__main__":
    array = [1, 2, 1]
    array.sort()
    k = 2
    out = []
    solve(array, k, out, 0, len(array))