# NA 15%

k = int(input())
s = input()
# 0 lower 1 upper
l1 = [0 if char.islower() else 1 for char in s]
l2 = []
for i, n in enumerate(l1):
    if i == 0:
        count = 1
    elif last == n:
        count += 1
    else:
        l2.append(count)
        count = 1
    last = n
l2.append(count)
l3 = []
for n in l2:
    if n == k:
        l3.append(1)
    elif n < k:
        l3.append(0)
    else:
        l3.append(2)
if 1 in l3:
    cur = 0
    m = 0
    for i in range(len(l3)):
        if l3[i] == 1:
            cur += 1
            if cur > m:
                m = cur
                end = i
        else:
            cur = 0
    extra = 0
    if l3[end] == 2:
        extra += 1
    if end-m > 0 and l3[end-m] == 2:
        extra += 1
    ans = m + extra
else:
    if 2 in l3:
        if any(l3[i] == 2 and l3[i + 1] == 2 for i in range(len(l3) - 1)):
            ans = 2*k
        else:
            ans = k
    else:
        ans = 0
print(ans)
