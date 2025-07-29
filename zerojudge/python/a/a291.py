# import sys

# lines = sys.stdin.read().splitlines()
# i = 0
# while i < len(lines):
#     while i < len(lines) and lines[i].strip() == '':
#         i += 1
#     if i >= len(lines):
#         break
#     passwd = list(map(int, lines[i].split()))
#     i += 1
#     n = int(lines[i])
#     i += 1
#     tries = []
#     for _ in range(n):
#         tries.append(list(map(int, lines[i].split())))
#         i += 1
#     for t in tries:
#         a = 0
#         b = 0
#         indexs = []
#         for j, (char, pwd) in enumerate(zip(t, passwd)):
#             if char == pwd:
#                 a += 1
#                 indexs.append(j)
#         if a != 4:
#             temp_pwd = passwd.copy()
#             temp_t = t.copy()
#             for j in sorted(indexs, reverse=True):
#                 temp_pwd.pop(j)
#                 temp_t.pop(j)
#             for char in temp_t:
#                 if char in temp_pwd:
#                     b += 1
#                     temp_pwd.pop(temp_pwd.index(char))
#         print(f"{a}A{b}B")

from sys import stdin
output = ''
for s in stdin:
    if s.strip() == '':
        continue
    pwd = s.split()
    dic = {str(k): 0 for k in range(10)}
    for i in pwd:
        dic[i] += 1
    n = int(stdin.readline())
    for _ in range(n):
        ans = stdin.readline().split()
        a, b, c, d = 0, 0, pwd[:], dic.copy()

        for j in range(4):
            if ans[j] == pwd[j]:
                d[str(pwd[j])] -= 1
                a = a + 1
                c[j] = 'o1'
                ans[j] = 'o2'
        for j in ans:
            if j in c and d[j] > 0:
                d[j] -= 1
                b = b + 1
        output = output + f'{a}A{b}B\n'
print(output)
