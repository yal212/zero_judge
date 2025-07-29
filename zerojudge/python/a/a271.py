N = int(input())
for _ in range(N):
    x, y, z, w, n, m = map(int, input().split())
    days = list(map(int, input().split()))
    poison_counter = 0
    died = False
    for day in days:
        m -= poison_counter * n
        if m <= 0:
            print("bye~Rabbit")
            died = True
            break
        if day == 0:
            pass
        elif day == 1:
            m += x
        elif day == 2:
            m += y
        elif day == 3:
            m -= z
        elif day == 4:
            m -= w
            poison_counter += 1
        if m <= 0:
            print("bye~Rabbit")
            died = True
            break
    if not died:
        print(f"{m}g")
