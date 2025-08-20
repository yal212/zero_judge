from sys import stdin
input = stdin.readline
K, Q, R = map(int, input().split())
s = list(input().strip())
P = [list(map(int, input().split())) for _ in range(Q)]
results = []
for p in P:
    new_s = [None] * K
    for i in range(K):
        new_s[p[i]-1] = s[i]
    s = new_s
    results.append(s.copy())
for j in range(R):
    line = []
    for i in range(Q):
        line.append(results[i][j])
    print("".join(line))