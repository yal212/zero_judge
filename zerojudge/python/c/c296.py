N, M, K = map(int, input().split())
# N, M, K = 5, 2, 4

people = [n+1 for n in range(N)]
now = 0

for _ in range(K):
    now += M-1
    now = now % len(people)
    # print(now, people)
    # print(people[now])
    people.pop(now)

now = now % len(people)

print(people[now])

# now 0 12345
# now 1 1"2"345
# now 2 1"2"3"4"5
# now 3=0 "12"3"4"5
