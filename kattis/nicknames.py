n_names = int(input())
names = [input() for _ in range(n_names)]
n_nicks = int(input())
nicks = [input() for _ in range(n_nicks)]

for nick in nicks:
    n = 0
    for name in names:
        check = name[:len(nick)]
        if check == nick:
            n += 1
    print(n)
