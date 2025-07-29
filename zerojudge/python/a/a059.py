n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    ans = 0
    for n in range(a, b+1):
        if int(n**0.5)**2 == n:
            ans += n
    print(f"Case {i+1}: {ans}")
