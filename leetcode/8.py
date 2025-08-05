class Solution:
    def myAtoi(self, s: str) -> int:
        ans = []
        positive = True
        sign = False
        for char in list(s):
            if char == " " and (len(ans) > 0 or sign):
                break
            elif char == " ":
                continue
            if not sign:
                if char == "-" and len(ans) == 0:
                    positive = False
                    sign = True
                    continue
                if char == "+" and len(ans) == 0:
                    sign = True
                    continue
            if not char.isdigit():
                break
            ans.append(char)
        ans = (int("".join(ans)) if positive else int(
            "-" + "".join(ans))) if ans else 0
        if ans < -(2**31):
            return -(2**31)
        if ans > 2**31 - 1:
            return 2**31 - 1
        return ans
