# TLE
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []

        def pro(num):
            p = 1
            for n in num:
                p *= n
            return p
        for i in range(len(nums)):
            right = nums[:i]
            left = nums[i+1:]
            l.append(pro(right)*pro(left))
        return l


# 17ms
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*len(nums)
        pre = 1
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(n-1, -1, -1):
            ans[i] *= post
            post *= nums[i]

        return ans
