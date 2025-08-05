n = int(input())
height = list(map(int, input().split()))
ans = 0

if height[0] == 0:
    ans += height[1]
if height[-1] == 0:
    ans += height[-2]
for i in range(1, n-1):
    if height[i] == 0:
        ans += min(height[i+1], height[i-1])

print(ans)
