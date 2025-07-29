l = int(input())
scores = list(map(int, input().split()))
passed = []
passx = []

for score in scores:
    if score >= 60:
        passed.append(score)
    else:
        passx.append(score)

print(*sorted(scores))

if passx == []:
    print("best case")
    print(min(passed))
elif passed == []:
    print(max(passx))
    print("worst case")
else:
    print(max(passx))
    print(min(passed))
