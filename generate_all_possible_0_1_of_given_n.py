count = 0
def generate_all_possible_0_1_of_given_n(n, op):
    global count
    if n == 0:
        print(op)
        count += 1
        return
    op1 = op + "1"
    op2 = op + "0"
    generate_all_possible_0_1_of_given_n(n-1, op1)
    generate_all_possible_0_1_of_given_n(n-1, op2)
    return count

if __name__ == "__main__":
    n = 3
    op = ""
    print(generate_all_possible_0_1_of_given_n(n, op))