n = int(input())
for _ in range(n):
    num = input()
    ans = 1
    for i in num:
        ans *= int(i)
    print(ans)
