from sys import stdin
for s in stdin:
    n = int(s)
    if n == 0:
        break
    b = bin(n)
    x = len(b)
    y = len(b.rstrip('1'))
    print(x - y)
