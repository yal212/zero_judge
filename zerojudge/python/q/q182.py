s = list(input())
k = int(input())
acts = list(int(input()) for _ in range(k))

for act in acts:
    if act == 0:
        for i in range(0, len(s), 2):
            s[i], s[i+1] = s[i+1], s[i]
    elif act == 1:
        for i in range(0, len(s), 2):
            temp = sorted([s[i], s[i+1]])
            s[i], s[i+1] = temp[0], temp[1]
    else:
        half = len(s)//2
        left = s[:half]
        right = s[half:]
        j = 0
        for i in range(0, len(s), 2):
            s[i], s[i+1] = left[j], right[j]
            j += 1
print("".join(s))
