def AND(a, b):
    if a != 0 and b != 0:
        return 1
    return 0


def OR(a, b):
    if a == 0 and b == 0:
        return 0
    return 1


def XOR(a, b):
    if (a == 0 and b == 0) or (a != 0 and b != 0):
        return 0
    return 1


while True:
    try:
        line = input()
        if not line.strip():
            continue
        if line[0].isalpha():
            print(line)
            continue
        a, b, target = map(int, line.split())
        impossible = True

        if target == AND(a, b):
            print("AND")
            impossible = False
        if target == OR(a, b):
            print("OR")
            impossible = False
        if target == XOR(a, b):
            print("XOR")
            impossible = False
        if impossible:
            print("IMPOSSIBLE")
    except:
        break
