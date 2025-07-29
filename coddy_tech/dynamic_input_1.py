n = int(input())
nums = [int(input()) for _ in range(n)]

ans = 0

for num in nums:
    ans += num

print(ans)
