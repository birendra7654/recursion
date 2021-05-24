def hanoi_tower(s, d, h, n):
    if n == 1:
        print(f"moving disk {n} from {s} to {d}")
        return
    hanoi_tower(s, h, d, n-1)
    print(f"moving disk {n} from {s} to {d}")
    hanoi_tower(h, d, s, n-1)
    # return count


if __name__ == "__main__":
    s = "source"
    d = "dest"
    h = "helper"
    n = 20
    print(hanoi_tower(s, d, h, n))