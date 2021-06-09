# Replace every array element with the product of every other element without using a division operator
# https://www.techiedelight.com/replace-element-array-product-every-element-without-using-division-operator/
# Input: {1, 2, 3, 4, 5}
# Output: {120, 60, 40, 30, 24}
#
# Input: {5, 3, 4, 2, 6, 8}
# Output: {1152, 1920, 1440, 2880, 960, 720}

def solve(array):
    left = [1] * len(array)
    right = [1] * len(array)
    for i in range(1, len(array)):
        left[i] = array[i-1] * left[i-1]

    for i in range(len(array)-2, -1, -1):
        right[i] = array[i+1] * right[i+1]

    for i in range(len(array)):
        print(left[i] * right[i])


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    solve(array)
