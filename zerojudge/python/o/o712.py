from sys import stdin
input = stdin.readline
M, N, k, r, c = map(int, input().split())
themap = [list(map(int, input().split())) for _ in range(M)]
score = 0
count = 0
dr = 1
def move(r, c, dr):
    for _ in range(4):
        lr, lc = r, c
        if dr == 0:
            r -= 1
        elif dr == 1:
            c += 1
        elif dr == 2:
            r += 1
        else:
            c -= 1
        if 0 <= r < M and 0 <= c < N and themap[r][c] != -1:
            return r, c, dr
        r, c = lr, lc
        dr = (dr + 1) % 4
    return False
while True:
    if themap[r][c] == 0:
        break
    score += themap[r][c]
    count += 1
    themap[r][c] -= 1
    if score % k == 0:
        dr = (dr + 1) % 4
    temp = move(r, c, dr)
    if not temp:
        break
    r, c, dr = temp
print(count)