while True:
    try:
        n = int(input())
        ans = (n**3 + 5*n + 6)//6
        print(ans)
    except EOFError:
        break
