n = int(input())
dir = int(input())  # 0 left 1 up 2 right 3 down
m = [list(map(int, input().split())) for _ in range(n)]
line = ""
r = c = n//2
line += str(m[r][c])
step = 1
step_counter = 0
turn_counter = 0


def changedir(dir):
    if dir != 3:
        return dir + 1
    else:
        return 0


for i in range(n**2-1):
    if dir == 0:
        c -= 1
    elif dir == 1:
        r -= 1
    elif dir == 2:
        c += 1
    else:
        r += 1
    line += str(m[r][c])
    step_counter += 1
    if step == step_counter:
        dir = changedir(dir)
        turn_counter += 1
        step_counter = 0
        if turn_counter % 2 == 0:
            step += 1


print(line)


#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
