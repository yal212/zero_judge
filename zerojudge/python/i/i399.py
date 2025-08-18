from sys import stdin
input = stdin.readline
A = list(map(int, input().split()))
counter = {}
ans = []
for a in A:
    if not counter.get(a, False):
        ans.append(a)
        counter[a] = 1
    else:
        counter[a] += 1
m = max(counter.values())
ans = sorted(ans, reverse=True)
result = [m]
for a in ans:
    result.append(a)
print(*result)
