num = int(input())
# Write your code below

nums = []
for n in range(1, num+1):
    if num % n == 0:
        nums.append(n)

for n in nums:
    print(f"{n} {int(num/n)}")
