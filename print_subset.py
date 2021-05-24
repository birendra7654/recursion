
def print_substring(string, res):
    if res:
        print("".join(res), end=" ")
    for i in range(len(string)):
        res.append(string[i])
        print_substring(string[i+1:], res)
        res.pop()


def print_subset(ip, op):
    if len(ip) == 0:
        print(op, end=",")
        return

    op1 = op
    op2 = op
    item = ip[0]
    op2 = op2 + item
    ip = "" if len(ip) == 1 else ip[1: ]
    print_subset(ip, op1)
    print_subset(ip, op2)
    return


if __name__ == "__main__":
    string = "abc"
    res = []
    # print_substring(string, res)
    ip = "abc"
    op = ""
    # ip = [i for i in ip]
    # op = []
    print_subset(ip, op)