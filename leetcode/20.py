class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        def match(c1, c2):
            return (c1 == "(" and c2 == ")") or (c1 == "[" and c2 == "]") or (c1 == "{" and c2 == "}")

        queue = [s[0]]
        for char in s[1:]:
            if char in "([{":
                queue.append(char)
            else:
                if not queue or not match(queue[-1], char):
                    return False
                queue.pop()
        return not queue
