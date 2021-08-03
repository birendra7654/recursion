# Find all permutations of a string in Python
# https://www.techiedelight.com/find-all-permutations-string-python/


def permutation(S, start, n):
    if start == n:
        print("".join(S))
        return

    for i in range(start, n):
        S[i], S[start] = S[start], S[i]
        permutation(S, start+1, n)
        S[i], S[start] = S[start], S[i]


if __name__ == "__main__":
    S = ["A", "B", "C"]
    n = len(S)
    permutation(S, 0, n)