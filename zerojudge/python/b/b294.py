n = int(input())
bought = list(map(int, input().split()))
cost = 1
total = 0

for buy in bought:
    total += cost*buy
    cost += 1

print(total)
