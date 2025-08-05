n = input()

if int(n) < 0:
    n = n[::-1]
    n = int(n[:-1])
    print(-n)
else:
    n = int(n[::-1])
    print(n)
