import os


def hanoi(n, a="A", b="B", c="C"):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("Move a Disc from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)


if __name__ == '__main__':
    # Ask for number of pieces to move
    hanoi(int(input("Enter total piece in tower : ")))
    os.system("cls")




