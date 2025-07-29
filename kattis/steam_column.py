n1 = int(input())
n2 = int(input())

n3 = abs(n1-n2)
if n3 > 180:
    n3 = 360-n3
print(n3)