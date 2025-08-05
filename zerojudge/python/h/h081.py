n, D = map(int, input().split())
a = list(map(int, input().split()))
profit = -a[0]
last_bought = a[0]
last_sell = None
stock = True
for i in range(1, n):
    y = a[i]
    if stock and y >= (last_bought+D):
        profit += y
        last_sell = y
        stock = False
    elif not stock and y <= (last_sell-D):
        profit -= y
        last_bought = y
        stock = True

if stock:
    profit += last_bought
print(profit)
