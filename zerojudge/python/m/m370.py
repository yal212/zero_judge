from sys import stdin
input = stdin.readline
x, n = map(int, input().split())
array = sorted(list(map(int, input().split())))
l, r = 0, 0
for i in range(n):
    pos = array[i]
    if pos < x:
        l += 1
    else:
        r += 1
if r > l:
    print(*[r, array[-1]])
else:
    print(*[l, array[0]])
