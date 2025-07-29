while True:
    try:
        rows, cols = map(int, input().split())
        A = []
        for _ in range(rows):
            temp = list(map(int, input().split()))
            A.append(temp)

        ans = [[0 for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                ans[c][r] = A[r][c]

        for row in ans:
            print(*row)
    except EOFError:
        break
