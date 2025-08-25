from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
pos = sorted(list(map(int, input().split())))
def check(l):
    now = pos[0] + l
    count = 1
    for i in pos:
        if i <= now:
            continue
        count += 1
        now = i + l
    return count <= k

L, R = 1, pos[-1] - pos[0]
ans = R
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1

print(ans)