def string_copy(str1, str2):
    if len(str1) == 0:
        return str2
    str2 = str2 + str1[0]
    str1 = "" if len(str1) == 1 else str1[1:]
    return string_copy(str1, str2)


if __name__ == "__main__":
    str1 = "hello"
    str2 = "geeksforgeeks"
    print(string_copy(str1, ''))