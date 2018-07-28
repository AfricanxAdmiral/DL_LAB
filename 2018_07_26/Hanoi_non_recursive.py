def solve(n):
    if n % 2:
        solve_odd(n)
    else:
        solve_even(n)


def solve_odd(n):
    # Three lists represent three parts of tower
    a = [0]
    b = [0]
    c = [0]

    # Initialize all
    for x in range(n):
        a.append(n - x)

    # Start solving
    count = 0
    while True:
        # First part
        if (len(c) == 1) or (a[-1] < c[-1] and a[-1] and c[-1]):
            disk = a.pop()
            print("Move Disc %s from A to C " % disk)
            c.append(disk)
            count += 1
        elif (len(a) == 1) or (a[-1] > c[-1] and a[-1] and c[-1]):
            disk = c.pop()
            print("Move Disc %s from C to A " % disk)
            a.append(disk)
            count += 1
        if count == 2**n - 1:
            break

        # Second part
        if (len(b) == 1) or (a[-1] < b[-1] and a[-1] and b[-1]):
            disk = a.pop()
            print("Move Disc %s from A to B " % disk)
            b.append(disk)
            count += 1
        elif (len(a) == 1) or (a[-1] > b[-1] and a[-1] and b[-1]):
            disk = b.pop()
            print("Move Disc %s from B to A " % disk)
            a.append(disk)
            count += 1
        if count == 2 ** n - 1:
            break

        # Third part
        if (len(c) == 1) or (b[-1] < c[-1] and b[-1] and c[-1]):
            disk = b.pop()
            print("Move Disc %s from C to B " % disk)
            c.append(disk)
            count += 1
        elif (len(b) == 1) or (b[-1] > c[-1] and b[-1] and c[-1]):
            disk = c.pop()
            print("Move Disc %s from B to C " % disk)
            b.append(disk)
            count += 1
        if count == 2 ** n - 1:
            break


def solve_even(n):
    # Three lists represent three parts of tower
    a = [0]
    b = [0]
    c = [0]

    # Initialize all
    for x in range(n):
        a.append(n - x)

    # Start solving
    count = 0
    while True:
        # First part
        if (len(b) == 1) or (a[-1] < b[-1] and a[-1] and b[-1]):
            disk = a.pop()
            print("Move Disc %s from A to B " % disk)
            b.append(disk)
            count += 1
        elif (len(a) == 1) or (a[-1] > b[-1] and a[-1] and b[-1]):
            disk = b.pop()
            print("Move Disc %s from B to A " % disk)
            a.append(disk)
            count += 1
        if count == 2 ** n - 1:
            break

        # Second part
        if (len(c) == 1) or (a[-1] < c[-1] and a[-1] and c[-1]):
            disk = a.pop()
            print("Move Disc %s from A to C " % disk)
            c.append(disk)
            count += 1
        elif (len(a) == 1) or (a[-1] > c[-1] and a[-1] and c[-1]):
            disk = c.pop()
            print("Move Disc %s from C to A " % disk)
            a.append(disk)
            count += 1
        if count == 2 ** n - 1:
            break

        # Third part
        if (len(c) == 1) or (b[-1] < c[-1] and b[-1] and c[-1]):
            disk = b.pop()
            print("Move Disc %s from C to B " % disk)
            c.append(disk)
            count += 1
        elif (len(b) == 1) or (b[-1] > c[-1] and b[-1] and c[-1]):
            disk = c.pop()
            print("Move Disc %s from B to C " % disk)
            b.append(disk)
            count += 1
        if count == 2 ** n - 1:
            break


if __name__ == '__main__':
    # Ask for number of disk to move
    solve(int(input("Enter total disk in tower : ")))
