# 1. TLE
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         def twosum(nums, target):
#             ans = []
#             for num in nums:
#                 if target-num in nums:
#                     if target-num == num and nums.count(num) >= 2:
#                         ans.append([num, num])
#                     elif target-num != num:
#                         ans.append([num, target-num])
#             return ans
#         for i in range(len(nums)):
#             if twosum(nums[:i]+nums[i+1:], 0-nums[i]):
#                 l = twosum(nums[:i]+nums[i+1:], 0-nums[i])
#                 for pair in l:
#                     if sorted([nums[i], pair[0], pair[1]]) not in ans:
#                         ans.append(sorted([nums[i], pair[0], pair[1]]))
#         return ans

# cheat 596ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, l-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans
