# 356ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_queue = []
        t_queue = []
        l = len(s)
        for i in range(l):
            if s[i] == t[i]:
                continue
            if s[i] not in t_queue:
                s_queue.append(s[i])
            else:
                t_queue.pop(t_queue.index(s[i]))
            if t[i] not in s_queue:
                t_queue.append(t[i])
            else:
                s_queue.pop(s_queue.index(t[i]))
        return not s_queue and not t_queue


# 13ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}
        for c in s:
            char[c] = char.get(c, 0) + 1
        for c in t:
            if c not in char:
                return False
            char[c] -= 1
            if char[c] == 0:
                del char[c]
        return not char
