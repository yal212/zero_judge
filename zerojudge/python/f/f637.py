expression = list(input())
n = int(input())
i = 0


def gettotal(n):
    global i
    exp = int(expression[i])
    i += 1
    if exp == 1:
        return n*n
    elif exp == 0:
        return 0
    elif exp == 2:
        return gettotal(n//2) + gettotal(n//2) + gettotal(n//2) + gettotal(n//2)


ans = gettotal(n)

print(ans)
