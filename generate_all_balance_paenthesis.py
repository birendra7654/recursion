res = []
def generate_balance_parenthesis(open, close, op):
    if open == 0 and close == 0:
        res.append(op)
        return
    if open == close:
        op1 = op + '('
        return generate_balance_parenthesis(open-1, close, op1)
    if open == 0:
        op1 = op + ")"
        return generate_balance_parenthesis(open, close-1, op1)
    else:
        op1 = op + "("
        op2 = op + ")"
        generate_balance_parenthesis(open-1, close, op1)
        generate_balance_parenthesis(open, close - 1, op2)


if __name__ == "__main__":
    n = 0
    open = n
    close = n
    op = ""
    generate_balance_parenthesis(open, close, op)
    print(res)