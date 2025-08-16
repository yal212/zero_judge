# NA (score:20%)
from sys import stdin
input = stdin.readline
M, N, j = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
start = None
for r, row in enumerate(Map):
    for c, val in enumerate(row):
        if val == -2:
            start = (r, c)
            break
    if start:
        break


def boom(Map, pos, rad):
    M, N = len(Map), len(Map[0])
    r, c = pos
    squares = set()
    squares.add((r, c))
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for step in range(1, rad+1):
            nr, nc = r + dr*step, c + dc*step
            if not (0 <= nr < M and 0 <= nc < N):
                break
            if Map[nr][nc] == -1:
                break
            squares.add((nr, nc))

    return list(squares)


area = 0
rad = 1
while area < j:
    area = 1
    queue = [start]
    visited = {start}
    while queue:
        pos = queue.pop(0)
        if pos == start:
            radius = rad
        else:
            radius = Map[pos[0]][pos[1]]
        squares = boom(Map, pos, radius)
        for square in squares:
            if square not in visited:
                queue.append(square)
                visited.add(square)
                area += 1
    if area < j:
        rad += 1
print(rad)
