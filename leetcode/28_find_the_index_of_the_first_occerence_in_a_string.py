class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        l = len(needle)
        i = 0
        while i+l <= len(haystack):
            if haystack[i:i+l] == needle:
                return i
            i += 1


# remove needle not in haystack as it isn't needed and increase time complexity
