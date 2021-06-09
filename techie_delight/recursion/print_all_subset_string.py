# Print all distinct subsets of a given set
# https://www.techiedelight.com/print-distinct-subsets-given-set/


def solve(s, n, out):
    if n > len(s)-1:
        print("1", "".join(out))
        return
    out.append(s[n])
    solve(s, n+1, out)
    out.pop()
    while n < len(s)-1 and s[n] == s[n+1]:
        n += 1
    solve(s, n+1, out)


if __name__ == "__main__":
    s = "xyx"
    s = "".join(sorted(s))
    n = len(s)
    out = []
    solve(s, 0, out)
