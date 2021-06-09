# Find all distinct combinations of a given length with repetition allowed k
#
# Input: {1, 2, 3}, k = 2
# Output: {1, 1}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 3}
#
# Input: {1, 2, 3, 4}, k = 2
# Output: {1, 1}, {1, 2}, {1, 3}, {1, 4}, {2, 2}, {2, 3}, {2, 4}, {3, 3}, {3, 4}, {4, 4}
#
# Input: {1, 2, 1}, k = 2
# Output: {1, 1}, {1, 2}, {2, 2}


# Function to print all distinct combinations of length `k`, where the
# repetition of elements is allowed
def findCombinations(A, out, k, i, n):
    # base case: if the combination size is `k`, print it
    if len(out) == k:
        print(out)
        return

    # start from the previous element in the current combination
    # till the last element
    j = i
    while j < len(A):
        # add current element `A[j]` to the solution and recur with the
        # same index `j` (as repeated elements are allowed in combinations)
        out.append(A[j])
        findCombinations(A, out, k, j, n)
        # backtrack: remove the current element from the solution
        out.pop()
        while j < n-1 and A[j] == A[j+1]:
            j += 1
        j += 1


if __name__ == '__main__':
    A = [1, 2, 1]
    A.sort()
    k = 2
    out = []
    findCombinations(A, out, k, 0, len(A))

