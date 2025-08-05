n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()
for xy in l:
    print(*xy)
