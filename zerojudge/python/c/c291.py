from collections import deque


# def findfriends(group):
#     for p in list(group)[-1]:
#         if friends[p] not in group:
#             group.add(friends[p])
#             return findfriends(group)
#     return group


def findfriends(start):
    group = set()
    queue = deque([start])
    while queue:
        p = queue.popleft()
        if p not in group:
            group.add(p)
            friend = friends[p]
            if friend not in group:
                queue.append(friend)
    return group


n = int(input())
peoples = list(map(int, input().split()))
friends = {i: peoples[i] for i in range(n)}
seen = set()
groups = 0
for i in range(n):
    if i not in seen:
        group = findfriends(i)
        seen.update(group)
        groups += 1
print(groups)
