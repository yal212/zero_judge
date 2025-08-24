class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1
        m = (p2 - p1) * min(height[p1], height[p2])
        while p1 != p2:
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            m = max(m, (p2 - p1) * min(height[p1], height[p2]))
        return m
