while True:
    try:
        def last(s):
            return (s[-1], -int(s))

        n = int(input())
        nums = list(map(str, input().split()))

        nums = sorted(nums, key=last)

        print(*nums)
    except:
        break
