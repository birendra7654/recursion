def reverse_stack_using_recusrion(stack):
    if len(stack) == 0:
        return
    n = stack.pop()
    reverse_stack_using_recusrion(stack)
    insert(stack, n)
    return stack


def insert(stack, n):
    if len(stack) == 0:
        stack.append(n)
        return stack
    item = stack.pop()
    insert(stack, n)
    stack.append(item)
    return stack


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(reverse_stack_using_recusrion(array))