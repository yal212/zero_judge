t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

l = {1: 31, 2: 60, 3: 91, 4: 121, 5: 151, 6: 181,
     7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
nl = {1: 31, 2: 59, 3: 90, 4: 120, 5: 150, 6: 180,
      7: 211, 8: 242, 9: 272, 10: 303, 11: 333, 12: 364}

ld = {1: 31, 2: 29, 3: 31, 4: 30, 5: 30, 6: 30,
      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
nld = {1: 31, 2: 28, 3: 31, 4: 30, 5: 30, 6: 30,
       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def find_bigger(t1, t2):
    if t1[0] > t2[0]:
        return [t1, t2]
    elif t1[0] < t2[0]:
        return [t2, t1]
    elif t1[1] > t2[1]:
        return [t1, t2]
    elif t1[1] < t2[1]:
        return [t2, t1]
    elif t1[2] > t2[2]:
        return [t1, t2]
    else:
        return [t2, t1]  # same date


t = find_bigger(t1, t2)
y1, m1, d1 = t[0]
y2, m2, d2 = t[1]

y = y1 - y2
m = m1 - m2
d = d1 - d2
dif = 0

if y == 0:
    if m == 0:
        dif = d
    else:
        pass
