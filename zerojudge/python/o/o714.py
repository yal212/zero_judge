# not done 
	# 1.	Dictionary overwrite – multiple buses with the same start lose data.
	# 2.	Incorrect visited – prevents revisiting positions via different routes.
	# 3.	DFS logic error – only stores start, ignores reachable positions correctly.
	# 4.	Partial counting – some valid paths never counted.
	# 5.	Inefficient traversal – BFS/DFS not needed; DP is simpler.
from sys import stdin
input = stdin.readline

n, m, p = map(int, input().split())

keys = list(map(int, input().split()))
values = list(map(int, input().split()))
buses = {}
for i in range(len(keys)):
    buses[keys[i]] = values[i]

ans = 0
visited = {0}
queue = [0]

while queue:
    cur = queue.pop()
    if buses[cur] == m:
        ans += 1
    for start, stop in buses.items():
        if cur <= start <= buses[cur] and (start not in visited) or stop == m:
            queue.append(start)
            visited.add(start)
print(ans%p)

