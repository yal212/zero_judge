n = int(input())
score = 0

if n >= 40:
    score = 100
if 40 > n >= 21:
    score += n-20
    n = 20
if 21 > n > 10:
    score += 2*(n-10)
    n = 10
if 11 > n > 0:
    score += 6*(n)

print(score)
