# n = int(input())
# s = [input() for _ in range(n)]
# ans = s[0]


# def check(s):
#     seen = {}
#     for char in s:
#         seen[char] = seen.get(char, 0) + 1
#     return seen


# for i in range(1, n):
#     s1, s2 = check(ans), check(s[i])
#     if len(s1) > len(s2):
#         ans = s[i]
#     elif len(s1) == len(s2):
#         for (k1, v1), (k2, v2) in zip(sorted(s1.items()), sorted(s2.items())):
#             if k1 > k2:
#                 ans = s[i]
#                 break
#             elif v1 > v2:
#                 ans = s[i]
#                 break

# print(ans)


def sort_key(x):
    return (len(set(x)), x)


n = int(input())
s = [input().strip() for _ in range(n)]

s.sort(key=sort_key)

print(s[0])
