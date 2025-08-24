class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        last = None
        m = 0
        for num in nums:
            if last is None:
                cur = 1
                last = num
            elif num == last:
                continue
            elif num == last+1:
                cur += 1
                last = num
            else:
                m = max(m, cur)
                cur = 1
                last = num
        m = max(m, cur)
        return m