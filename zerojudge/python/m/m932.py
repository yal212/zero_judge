from sys import stdin
input = stdin.readline
m, n, k = map(int, input().split())
Map = [list(map(str, input().strip())) for _ in range(m)]
moves = list(map(int, input().split()))
path = []
visited = set()
r, c = m-1, 0
for move in moves:
    if move == 0:
        nr = r-1
        if 0 <= nr:
            r = nr
    elif move == 1:
        nc = c+1
        if nc < n:
            c = nc
    elif move == 2:
        nr = r+1
        nc = c+1
        if nr < m and nc < n:
            r = nr
            c = nc
    elif move == 3:
        nr = r+1
        if nr < m:
            r = nr
    elif move == 4:
        nc = c-1
        if 0 <= nc:
            c = nc
    else:
        nr = r-1
        nc = c-1
        if 0 <= nr and 0 <= nc:
            r = nr
            c = nc
    new = Map[r][c]
    path.append(new)
    if new not in visited:
        visited.add(new)
print("".join(path))
print(len(visited))