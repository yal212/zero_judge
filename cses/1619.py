import sys
input = sys.stdin.readline
n = int(input())
# time = sorted(time)
times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, 1))
    times.append((end, -1))

s = sorted(times)
now = 0
m = 0
for t, i in s:
    now += i
    m = max(m, now)
print(m)
