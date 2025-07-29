n1, operater, n2 = input().split()
n1, n2 = int(n1), int(n2)


def add(a, b):
    return int(a+b)


def sub(a, b):
    return int(a-b)


def mul(a, b):
    return int(a*b)


def div(a, b):
    return a//b


if operater == "+":
    print(add(n1, n2))
elif operater == "-":
    print(sub(n1, n2))
elif operater == "*":
    print(mul(n1, n2))
elif operater == "/":
    print(div(n1, n2))
