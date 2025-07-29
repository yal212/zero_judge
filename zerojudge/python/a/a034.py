while True:
    try:
        n = int(input())
        ans = ""
        while n > 0:
            ans += str(n % 2)
            n = n//2
        ans = ans[::-1]
        print(ans)
    except EOFError:
        break
