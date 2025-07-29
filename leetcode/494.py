nums = [1, 1, 1, 1, 1]
target = 3


def findsums(nums, target):
    if sum(nums) % 2 != target % 2:
        return 0
    if sum(nums) < abs(target):
        return 0
    new_sums = {}
    for num in nums:
        for s, c in old_sums.items():
            new_sums[s+num] = new_sums.get(s+num, 0) + c
            new_sums[s-num] = new_sums.get(s-num, 0) + c
        old_sums, new_sums = new_sums, {}

    return old_sums.get(target, 0)


print(findsums(nums, target))

# decide minus how much from total sum
# and only need to run < (total-target)/2
