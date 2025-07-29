h1 = list(map(int, input().split()))
g1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
g2 = list(map(int, input().split()))

wins = 0

if sum(h1) > sum(g1):
    wins += 1
if sum(h2) > sum(g2):
    wins += 1

print(f"{sum(h1)}:{sum(g1)}")
print(f"{sum(h2)}:{sum(g2)}")

if wins == 2:
    print("Win")
elif wins == 1:
    print("Tie")
else:
    print("Lose")
