from sys import stdin
input = stdin.readline
s, t, n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(s)]
b = [list(map(int, input().split())) for _ in range(n)]

def d(x, y):
    dis = 0
    dif = 0
    for i in range(s):
        for j in range(t):
            if x[i][j] != y[i][j]:
                dif += y[i][j] - x[i][j]
                dis += 1
    return dis, dif

count = 0
mind = float("inf")
for i in range(n-s+1):
    for j in range(m-t+1):  # now list out of range
        now = [[b[i+q][j+p] for p in range(t)] for q in range(s)]
        dis, dif = d(a, now)
        if dis <= r:
            count += 1
            mind = min(mind, abs(dif))
print(count)
print(mind if count!=0 else -1)
