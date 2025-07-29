small, big = map(int, input().split())
ans = []
for i in range(small, big+1):
    amstrom = 0
    for num in str(i):
        amstrom += int(num)**len(str(i))
    if i == amstrom:
        ans.append(i)
if ans != []:
    print(*ans)
else:
    print("none")
