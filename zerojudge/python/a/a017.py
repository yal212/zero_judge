import sys


def break_brackets(line):
    for index, char in enumerate(line):
        if char == "(":
            line[index] = " "
            start_i = index
        break
    for index, char in enumerate(line):
        if char == ")":
            line[index] = " "
            end_i = index
        break


while True:
    try:
        line = map(str, input().split())
        ans = 0
        temp = 0
    except EOFError:
        break


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0


def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b  # 整除，題目保證不會有小數
    elif op == '%':
        return a % b


def calculate_expression(tokens):
    values = []
    ops = []

    def apply_top_op():
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    for t in tokens:
        if t == '(':
            ops.append(t)
        elif t == ')':
            while ops and ops[-1] != '(':
                apply_top_op()
            ops.pop()  # 拿掉 '('
        elif t in '+-*/%':
            while ops and ops[-1] != '(' and precedence(ops[-1]) >= precedence(t):
                apply_top_op()
            ops.append(t)
        else:
            # 數字
            values.append(int(t))

    while ops:
        apply_top_op()

    return values[0]


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    tokens = line.split()
    result = calculate_expression(tokens)
    print(result)
