def permutation_with_case_change(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op + ip[0]
    op2 = op + ip[0].upper()
    ip = "" if len(ip) == 1 else ip[1: ]
    permutation_with_case_change(ip, op1)
    permutation_with_case_change(ip, op2)


if __name__ == "__main__":
    ip = "abc"
    op = ""
    permutation_with_case_change(ip, op)