# TLE

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        def contain(s, t):
            for c in t:
                if t.count(c) > s.count(c):
                    return False
            return True
        left, right = 0, 0
        cur = s[0]
        min_s = ""
        while left <= right < len(s):
            while not contain(cur, t) and left <= right < len(s):
                right += 1
                cur = s[left:right+1]
            if contain(cur, t) and (min_s == "" or len(cur) < len(min_s)):
                min_s = cur
            while contain(cur, t) and left <= right:
                if min_s == "" or len(cur) < len(min_s):
                    min_s = cur
                left += 1
                cur = s[left:right+1]
        return min_s
