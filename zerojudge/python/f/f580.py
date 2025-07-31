#   3
# 5 1 2 6
#   4
# front roll ->
#   6
# 5 3 2 4
#   1
# right roll ->
#   3
# 6 5 2 1
#   4
n, m = map(int, input().split())
dices = [[5, 3, 1, 4, 2, 6] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    if b > 0:
        dices[a-1], dices[b-1] = dices[b-1], dices[a-1]
    elif b == -1:
        dice = dices[a-1]
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif b == -2:
        dice = dices[a-1]
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]

for dice in dices:
    print(dice[2], end=" ")
