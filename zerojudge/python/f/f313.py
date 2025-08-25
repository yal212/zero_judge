from sys import stdin
input = stdin.readline
R, C, k, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

for _ in range(m):
    next_matrix = [row[:] for row in matrix]  # copy
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == -1:  # no city
                continue
            move = matrix[i][j] // k
            if move == 0:
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] != -1:
                    next_matrix[i][j] -= move
                    next_matrix[ni][nj] += move
    matrix = next_matrix
ma = -float('inf')
mi = float('inf')
for i in range(R):
    for j in range(C):
        if matrix[i][j] != -1:
            ma = max(ma, matrix[i][j])
            mi = min(mi, matrix[i][j])
print(mi)
print(ma)
