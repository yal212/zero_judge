n = int(input())
ans = []

for i in range(1, n//2 + 1):
    if n % i == 0:
        ans.append(i)
        ans.append(n//i)

ans = list(set(ans))
ans.sort()
print(*ans)
