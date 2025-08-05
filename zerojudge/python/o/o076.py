n = int(input())
h = list(map(int, input().split()))
m = cur = 1

for i in range(0, n-1):
    if h[i] > h[i+1]:
        cur += 1
    else:
        cur = 1
    m = max(m, cur)

print(m)
