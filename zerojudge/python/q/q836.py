k = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
pos = 0

while k > 0:
    pos += k
    if pos % x1 == 0:
        k -= y1
    if pos % x2 == 0:
        k -= y2

print(pos)
