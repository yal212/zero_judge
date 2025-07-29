while True:
    try:
        l = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        print(*nums)
    except EOFError:
        break
