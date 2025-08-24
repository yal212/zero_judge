# cheat
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(max_sum, cur_sum)
        return max_sum


#
def maxSubArray(nums) -> int:
    def cross(nums):
        l = len(nums)
        r_max, l_max = -float("inf"), -float("inf")
        r_count = l_count = 0
        for i in range(l//2+1):
            r_count = r_count if l//2+i >= l else r_count+nums[l//2+i]
            l_count = l_count if l//2-i-1 < 0 else l_count+nums[l//2-i-1]
            r_max = max(r_max, r_count)
            l_max = max(l_max, l_count)
        # print(nums, l_max, r_max)
        return r_max+l_max

    def m(nums):
        if len(nums) == 1:
            return nums[0]
        l = len(nums)//2
        return max(m(nums[:l]), m(nums[l:]), cross(nums))
    return m(nums)


# print(maxSubArray(nums))
