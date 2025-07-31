n = int(input())


def A(l1, l2):
    if l1[1] == l1[3]:
        return False
    if l1[1] != l1[5]:
        return False
    if l2[1] == l2[3]:
        return False
    if l2[1] != l2[5]:
        return False
    return True


def B(l1, l2):
    if l1[-1] != 1:
        return False
    if l2[-1] != 0:
        return False
    return True


def C(l1, l2):
    if l1[1] == l2[1]:
        return False
    if l1[3] == l2[3]:
        return False
    if l1[5] == l2[5]:
        return False
    return True


for _ in range(n):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    ans = "None"
    if not A(l1, l2):
        ans = "A"
    if not B(l1, l2):
        if ans == "None":
            ans = "B"
        else:
            ans += "B"
    if not C(l1, l2):
        if ans == "None":
            ans = "C"
        else:
            ans += "C"
    print(ans)
