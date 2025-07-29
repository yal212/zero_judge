while True:
    try:
        n, m = map(int, input().split())
        count = 0
        ans = 0
        while True:
            count += n
            n += 1
            ans += 1
            if count > m:
                break
        print(ans)
    except EOFError:
        break
