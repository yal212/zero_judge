num = int(input())

powers = {}
ans = ""

for d in range(2, num+1):
    if num == 1:
        break
    power = 0
    while num%d == 0:
        num = num//d
        power += 1
    if power > 0:
        powers.update({d: power})

for nums in powers:
    if powers[nums] == 1:
        ans += str(nums) + " * " 
    else:
        ans += str(nums) + "^" + str(powers[nums]) + " * "

ans = ans[:-3]
print(ans)