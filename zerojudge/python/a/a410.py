a, b, c, d, e, f = map(int, input().split())

D = a*e - b*d
Dx = c*e - b*f
Dy = a*f - c*d

if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"x={x:.2f}")
    print(f"y={y:.2f}")
else:
    if Dx == 0 and Dy == 0:
        print("Too many")
    else:
        print("No answer")
