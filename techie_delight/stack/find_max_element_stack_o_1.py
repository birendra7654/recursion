
def solve(array, n, max):
    if len(array) == 0:
        return
    top = array.pop()
    if top > max:
        max = top
    solve(array, n, max)
    return max



if __name__ == "__main__":
    array = [4, 9, 2, 1, 7]
    max = -99999
    print(solve(array, len(array)-1, max))