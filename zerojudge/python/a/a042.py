while True:
    try:
        n = int(input())
        ans = n**2 - n + 2
        print(ans)
    except EOFError:
        break
