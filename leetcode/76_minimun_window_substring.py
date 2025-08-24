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


# cheat
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dict_t = {}
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        l = len(dict_t)
        got = 0
        left, right = 0, 0
        cur = {}
        ans = (float("inf"), None, None)
        while right < len(s):
            char = s[right]
            cur[char] = cur.get(char, 0) + 1
            if char in dict_t and cur[char] == dict_t[char]:
                got += 1
            while left <= right and got == l:
                char = s[left]
                if right-left+1 < ans[0]:
                    ans = (right-left+1, left, right)
                cur[char] -= 1
                if char in dict_t and cur[char] < dict_t[char]:
                    got -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
