t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    d = l[1]-l[0]
    r = l[1]/l[0]
    if l[1]+d == l[2]:
        print(*l, int(l[3]+d))
    else:
        print(*l, int(l[3]*r))