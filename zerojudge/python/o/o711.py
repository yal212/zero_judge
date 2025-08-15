from sys import stdin
input = stdin.readline
n = int(input())
w1, w2, h1, h2 = map(int, input().split())
fills = map(int, input().split())
cur = 0
m = 0
a1 = w1*w1
a2 = w2*w2
v1 = a1*h1
v2 = a2*h2
full = v1+v2

for fill in fills:
    if cur >= full:
        break
    elif cur+fill >= full:
        if cur >= v1:
            m = max(m, (full-cur)//a2)
        else:
            m = max(m, (v1-cur)//a1+h2)
        cur = full
    elif cur+fill > v1:
        if cur >= v1:
            m = max(m, fill//a2)
        else:
            m = max(m, (v1-cur)//a1+(fill-(v1-cur))//a2)
        cur += fill
    else:
        m = max(m, fill//a1)
        cur += fill
print(m)