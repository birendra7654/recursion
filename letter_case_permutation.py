def letter_case_permutation(ip: str, op: str):
    if len(ip) == 0:
        print(op)
        return
    if ip[0].isdigit():
        op = op + ip[0]
        ip = "" if len(ip) == 1 else ip[1: ]
        letter_case_permutation(ip, op)
    else:
        op1 = op + ip[0].lower()
        op2 = op + ip[0].upper()
        ip = "" if len(ip) == 1 else ip[1:]
        letter_case_permutation(ip, op1)
        letter_case_permutation(ip, op2)


if __name__ == "__main__":
    ip = "A1B2"
    op = ""
    letter_case_permutation(ip, op)