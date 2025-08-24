# TLE
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def Anagrams(s1, s2):
            char = {}
            for c in s1:
                char[c] = char.get(c, 0) + 1
            for c in s2:
                if c not in char:
                    return False
                char[c] -= 1
                if char[c] == 0:
                    del char[c]
            return not char
        groups = []
        for s in strs:
            ingroup = False
            if not groups:
                groups.append([s])
                continue
            for group in groups:
                if Anagrams(s, group[0]):
                    group.append(s)
                    ingroup = True
                    continue
            if not ingroup:
                groups.append([s])
        return groups


# 9ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in groups:
                groups[ss] = []
            groups[ss].append(s)
        return list(groups.values())
