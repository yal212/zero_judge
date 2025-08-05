# 0指石頭，2指剪刀，5指布
def check(bro, sis):  # 0 win 1 draw 2 lose
    if bro == sis:
        return 1
    elif (bro == 0 and sis == 2) or (bro == 2 and sis == 5) or (bro == 5 and sis == 0):
        return 0
    else:
        return 2


F = []
F.append(int(input()))
N = int(input())
y = list(map(int, input().split()))

for i in range(N):
    if i > 0:
        if i >= 2 and y[i - 1] == y[i - 2]:
            if y[i - 1] == 0:
                F.append(5)
            elif y[i - 1] == 2:
                F.append(0)
            else:
                F.append(2)
        else:
            F.append(y[i - 1])

    result = check(F[i], y[i])
    if result == 0:
        print(*F, f": Won at round {i + 1}")
        break
    elif result == 2:
        print(*F, f": Lost at round {i + 1}")
        break
else:
    print(*F, f": Drew at round {N}")
