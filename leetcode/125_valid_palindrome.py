# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.strip()
#         s = "".join(c.lower() for c in s if c.isalnum())
#         l = len(s)
#         for i in range(l//2):
#             if s[i] != s[l-1-i]:
#                 return False
#         return True

# use two pointer for better result

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
