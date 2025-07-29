n, d = map(int, input().split())
items = list(list(map(int, input().split())) for _ in range(n))
buy = 0
cost = 0
for item in items:
    if (max(item) - min(item)) >= d:
        buy += 1
        cost += sum(item)//len(item)
print(buy, cost)
