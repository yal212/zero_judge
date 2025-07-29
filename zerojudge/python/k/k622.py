n, max_weight = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

backpack = {0: 0}

for weight, value in zip(weights, values):
    temp_bp = list(backpack.items())
    for w, v in temp_bp:
        if weight + w > max_weight:
            continue
        backpack[weight + w] = max(backpack.get(weight + w, 0), value + v)

print(max(backpack.values()))
