m, n, k = map(int, input().split())
words = [input() for _ in range(m)]
rotate_d = [list(map(int, input().split())) for _ in range(k)]
score = 0

for rd in rotate_d:
    for i, d in enumerate(rd):
        d %= n
        words[i] = words[i][-d:] + words[i][:-d]
    for i in range(n):
        value = {}
        for word in words:
            char = word[i]
            value[char] = value.get(char, 0) + 1
        score += max(value.values())

print(score)
