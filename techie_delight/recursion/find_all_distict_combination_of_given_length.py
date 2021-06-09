# Find all distinct combinations of a given length – I

# Input = {1, 2, 3} ,  k =2
# output = {1, 2}, {1, 3}, {2, 3}

# Input = {1, 2, 1} ,  k =2
# output = {1, 2}, {1, 1}
def solve(A, k, out, start, n):
    if len(out) == k:
        print(out)
        return
    i = start
    while i < n:
        out.append(A[i])
        solve(A, k, out, i+1, n)
        out.pop()
        while i < n-1 and A[i] == A[i+1]:
            i += 1
        i += 1


if __name__ == "__main__":
    A = [1, 2, 1]
    k = 2
    A.sort()
    out = []
    solve(A, k, out, 0, len(A))
