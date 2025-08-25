# stack

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        queue = [("", 0, 0)]
        while queue:
            cur, op, cl = queue.pop()
            if len(cur) == n*2:
                ans.append(cur)
                continue
            if op < n:
                queue.append((cur+"(", op+1, cl))
            if cl < op:
                queue.append((cur+")", op, cl+1))
        return ans
    

# backtracking

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bt(s, op, cl):
            if len(s) == n*2:
                ans.append(s)
                return
            if op < n:
                bt(s+"(", op+1, cl)
            if cl < op:
                bt(s+")", op, cl+1)
        bt("", 0, 0)
        return ans