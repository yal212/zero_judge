N, M = map(int, input().split())
groups = [list(map(int, input().split())) for _ in range(N)]
ms = 0
nums = []
yes = []
for group in groups:
    ms += max(group)
    nums.append(max(group))
print(ms)
for num in nums:
    if ms % num == 0:
        yes.append(num)
if not yes:
    print("-1")
else:
    print(*yes)
