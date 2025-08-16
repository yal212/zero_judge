from sys import stdin
input = stdin.readline
n = int(input())
dic = {}
for _ in range(n):
    a, d = map(int, input().split())
    total = a*a + d*d
    dic[total] = (a, d)
index = sorted(list(dic.keys()))[-2]
print(*dic[index])
