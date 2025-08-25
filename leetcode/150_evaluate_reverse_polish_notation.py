class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        queue = [tokens[0], tokens[1]]
        exp = "+-*/"
        cur = 2
        while cur < len(tokens):
            if tokens[cur] in exp:
                n2 = int(queue.pop())
                n1 = int(queue.pop())
                if tokens[cur] == "+":
                    result = n1 + n2
                elif tokens[cur] == "-":
                    result = n1 - n2
                elif tokens[cur] == "*":
                    result = n1 * n2
                else:
                    result = int(n1 / n2)
                queue.append(result)
            else:
                queue.append(int(tokens[cur]))
            cur += 1
        return queue.pop()