class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if int(x) >= 0:
            ans = int(x[::-1])
        else:
            x = x[1:]
            ans = (-int(x[::-1]))
        if abs(ans) > 2**31-1:
            return 0
        return ans
