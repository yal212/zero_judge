n, limit, over_weight_bill = map(int, input().split())

cases = [tuple(map(int, input().split())) for _ in range(n)]
total_w = 0

costs = {0: 0}

for weight, cost in cases:
    total_w += weight
    temp = list(costs.items())
    for w, c in temp:

        new_weight = w + weight
        new_cost = c + cost
        costs[weight + w] = min(costs.get(weight + w, float('inf')), cost + c)


for w, c in costs.items():
    if total_w-w > limit:
        costs[w] += (total_w-w-limit)*over_weight_bill

print(min(costs.values()))
