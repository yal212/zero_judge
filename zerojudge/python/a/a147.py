while True:
    try:
        n = int(input())
        ans = []
        for i in range(1, n):
            if i % 7 != 0:
                ans.append(i)
        print(*ans)
    except:
        break
