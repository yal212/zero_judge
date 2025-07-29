n = 4
x = 1


def find(n, x):
    done = {}

    def ffind(target, now):
        if target == 0:
            return 1
        if target < 0 or now == 0:
            return 0
        if (target, now) in done:
            return done[(target, now)]
        done[(target, now)] = (ffind(target, now-1) +
                               ffind(target-now**x, now-1)) % (10**9+7)
        return done[(target, now)]
    return ffind(n, int(n**(1/x)+1))


print(find(n, x))
