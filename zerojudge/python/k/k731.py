from sys import stdin
input = stdin.readline
n = int(input())
cords = [tuple(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
left, right, re = 0, 0, 0
dir = 1    # 0 1 2 3 up right down left
for cord in cords:
    nx, ny = cord[0], cord[1]
    if abs(nx-x) > 0:
        if nx-x > 0:
            if dir == 0:
                right += 1
            elif dir == 2:
                left += 1
            elif dir == 3:
                re += 1
            dir = 1
        else:
            if dir == 0:
                left += 1
            elif dir == 1:
                re += 1
            elif dir == 2:
                right += 1
            dir = 3
    elif abs(ny-y) > 0:
        if ny-y > 0:
            if dir == 1:
                left += 1
            elif dir == 2:
                re += 1
            elif dir == 3:
                right += 1
            dir = 0
        else:
            if dir == 0:
                re += 1
            elif dir == 1:
                right += 1
            elif dir == 3:
                left += 1
            dir = 2
    x, y = nx, ny
print(*[left, right, re])
