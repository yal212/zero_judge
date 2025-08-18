from sys import stdin
input = stdin.readline
n = int(input())
stops = [list(map(int, input().split())) for _ in range(n)]
d = []
def m(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
for i in range(n-1):
    stop = stops[i]
    d.append(m(stop, stops[i+1]))
d = sorted(d)
print(*[d[-1], d[0]])