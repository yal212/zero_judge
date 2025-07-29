a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())


def y1(x):
    return int(a1*x*x + b1*x + c1)


def y2(x):
    return int(a2*x*x + b2*x + c2)


for i in range(n+1):
    t = y1(i) + y2(n-i)
    if i == 0:
        m = t
    elif t > m:
        m = t
print(m)
