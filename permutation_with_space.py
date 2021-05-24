def permutation_with_spaces(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op + ip[0]
    op2 = op
    op2 = op2 + "-" + ip[0]
    ip = "" if len(ip) == 1 else ip[1: ]
    permutation_with_spaces(ip, op1)
    permutation_with_spaces(ip, op2)


if __name__ == "__main__":
    ip = "ABCD"
    op = ip[0]
    ip = ip[1:]
    permutation_with_spaces(ip, op)