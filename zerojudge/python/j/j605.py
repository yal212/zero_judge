from sys import stdin
input = stdin.readline
n = int(input())
score = {}
ms = -1
error = 0
for _ in range(n):
    t, s = map(int, input().split())
    score[t] = s
    if s > ms:
        ms, mst = s, t
    elif s == -1:
        error += 1
total = ms-n-error*2
total = total if total>0 else 0
ans = [total, mst]
print(*ans)