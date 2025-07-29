_str = input()
k = 7
ans = ""

for i in _str:
    ans += chr(ord(i)-k)

print(ans)