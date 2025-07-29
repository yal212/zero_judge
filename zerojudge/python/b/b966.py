# n = int(input())
# lines = [list(map(int, input().split())) for _ in range(n)]
# area = set()
# for line in lines:
#     d1 = line[0]
#     d2 = line[1]
#     l = d2 - d1
#     if l == 0:
#         continue
#     for a in range(d1, d2):
#         area.add(a)
# print(len(area))


n = int(input())
lines = [tuple(sorted(map(int, input().split()))) for _ in range(n)]
lines.sort()
merged = []
for start, end in lines:
    if start == end:
        continue
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
total = sum(end - start for start, end in merged)
print(total)
