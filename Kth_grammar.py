def kth_grammer(n, k):
    if n == 1 and k == 1:
        return 0
    mid = pow(2, n-1) // 2
    # print(mid)
    if k <= mid:
        return kth_grammer(n-1, k)
    else:
        return not kth_grammer(n-1, k-mid)


if __name__ == "__main__":
    n = 4
    k = 3

    print(kth_grammer(n, k))