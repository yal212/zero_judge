from collections import defaultdict


def findJudge(n: int, trust) -> int:
    relation = {}
    for a, b in trust:
        if not relation.get(a, False):
            relation[a] = [b]
        else:
            relation[a].append(b)
    # print(relation)
    onejudge = False
    for i in range(1, n+1):
        if not relation.get(i, False):
            if onejudge:
                return -1
            onejudge = i
    # print(onejudge)
    for t in relation.values():
        if onejudge not in t:
            return -1
    return onejudge


n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(findJudge(n, trust))


class Solution:
    def findJudge(self, n: int, trust) -> int:
        relation = defaultdict(list)
        for a, b in trust:
            relation[a].append(b)
        onejudge = False
        for i in range(1, n+1):
            if not relation.get(i, False):
                if onejudge:
                    return -1
                onejudge = i
        for t in relation.values():
            if onejudge not in t:
                return -1
        return onejudge
