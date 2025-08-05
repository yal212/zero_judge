a, b = map(int, input().split())
n = int(input())
lap_time = list(map(int, input().split()))
s = a + b
time = 0
for t in lap_time:
    if s > t:
        if a > t:
            continue
        else:
            time += b - (t-a)
    else:
        extra = t % s
        if extra >= a:
            time += b - (extra - a)
        else:
            continue
print(time)
