class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        cur = []
        for char in s:
            if char in cur:
                cur = cur[cur.index(char)+1:]
            cur.append(char)
            m = max(m, len(cur))
        return m
