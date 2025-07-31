class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if (target - n) in nums:
                if (target - n) == n:
                    if nums.count(n) >= 2:
                        nums.pop(i)
                        return [i, nums.index(n)+1]
                else:
                    return [i, nums.index(target-n)]
