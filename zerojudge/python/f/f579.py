a, b = map(int, input().split())
n = int(input())
custom = 0
for _ in range(n):
    actions = list(map(int, input().split()))
    if actions.count(a) > actions.count(-a) and actions.count(b) > actions.count(-b):
        custom += 1
print(custom)
