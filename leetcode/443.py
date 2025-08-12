# cheat
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        i = 0
        while i < len(chars):
            cur = chars[i]
            count = 1
            i += 1

            while i < len(chars) and chars[i] == cur:
                count += 1
                i += 1
            ans.append(cur)
            if count > 1:
                for n in str(count):
                    ans.append(n)
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)
