# Print N-bit binary numbers having more 1’s than 0’s for any prefix

def N_bit_binary_number_prefix_1_more_than_0(one, zero, n, op):
    if n == 0:
        print(op)
        return
    op1 = op + "1"
    N_bit_binary_number_prefix_1_more_than_0(one+1, zero, n-1, op1)
    if one > zero:
        op2 = op + "0"
        N_bit_binary_number_prefix_1_more_than_0(one, zero + 1, n - 1, op2)


if __name__ == "__main__":
    one = 0
    zero = 0
    n = 3
    op = ""
    N_bit_binary_number_prefix_1_more_than_0(one, zero, n, op)
