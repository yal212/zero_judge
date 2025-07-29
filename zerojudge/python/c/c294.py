l = list(map(int, input().split()))
l.sort()
a, b, c = l[0], l[1], l[2]
ab = a*a + b*b
c2 = c*c
print(*l)
if a+b <= c:
    print("No")
elif ab > c2:
    print("Acute")
elif ab < c2:
    print("Obtuse")
else:
    print("Right")
