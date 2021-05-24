def remove_middle_element_from_stack(stack, k):
    if k == 0:
        stack.pop()
        return
    n = stack.pop()
    remove_middle_element_from_stack(stack, k-1)
    stack.append(n)
    return stack



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    k = len(array)//2 + 1
    print(k)
    print(remove_middle_element_from_stack(array, k-1))