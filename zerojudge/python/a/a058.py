n = int(input())
k1 = 0
k2 = 0
k3 = 0

for i in range(n):
    num = int(input())
    if num % 3 == 0:
        k1 += 1
    elif num % 3 == 1:
        k2 += 1
    else:
        k3 += 1

print(k1, k2, k3)
