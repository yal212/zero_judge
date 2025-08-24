class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        cur = strs[0]
        for s in strs[1:]:
            i = 0
            temp = ""
            while i < len(cur) and i < len(s) and cur[i] == s[i]:
                temp += cur[i]
                i += 1
            cur = temp
        return cur
