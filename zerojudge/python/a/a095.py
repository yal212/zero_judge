while True:
    try:
        n, m = map(int, input().split())
        if n == m:
            print(m)
        else:
            print(m+1)
    except:
        break
