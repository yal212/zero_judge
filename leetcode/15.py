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
