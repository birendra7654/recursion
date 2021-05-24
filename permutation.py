
result = []
def permutation(list_string, start, n):
    if start == n:
        result.append(''.join(list_string))
    for j in range(start, n):
        list_string[start], list_string[j] = list_string[j], list_string[start]
        permutation(list_string, start+1, n)
        list_string[start], list_string[j] = list_string[j], list_string[start]


if __name__ == "__main__":
    string = "ABC"
    list_string = list(map(lambda x: x, string))
    permutation(list_string, 0, len(string))
    print(result)