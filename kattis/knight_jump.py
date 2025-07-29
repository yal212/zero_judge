size = int(input())
field = []
for i in range(size):
    _input = input()
    for ij, j in enumerate(_input):
        if j == "K":
            start = (i, ij)
    field.append(_input)

directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
              (1, -2), (1, 2), (2, -1), (2, 1)]

visited = {start: 0}
queue = [start]
while queue:
    step = visited[queue[0]]
    x, y = queue.pop(0)
    if x == y == 0:
        # print(step)
        break
    for dx, dy in directions:
        _x = x+dx
        _y = y+dy
        if 0 <= _x < size and 0 <= _y < size and field[_x][_y] != "#" and (_x, _y) not in visited:
            visited[(_x, _y)] = step+1
            queue.append((_x, _y))
print(visited.get((0, 0), -1))

# size=int(input())
# field=[]
# for i in range(size):
#     inp=input()
#     if "K" in inp:
#         start=(i,inp.index("K"))
#     field.append(inp)

# direction=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

# # visited as point
# visited={start}
# queue=[[*start,0]]

# while queue:
#     x,y,step=queue.pop(0)
#     if x==y==0:
#         print(step)
#         break
#     for dx,dy in direction:
#         if 0<=x+dx<size and 0<=y+dy<size and  field[x+dx][y+dy]!="#" and (x+dx,y+dy) not in visited:
#             visited.add((x+dx,y+dy))
#             queue.append([x+dx,y+dy,step+1])

# # visited as matrix
# visited=[[-1]*size for _ in range(size)]
# visited[start[0]][start[1]]=0
# queue=[start]
# while queue:
#     x,y=queue.pop(0)
#     if x==y==0:
#         print(visited[x][y])
#         break
#     for dx,dy in direction:
#         if 0<=x+dx<size and 0<=y+dy<size and  field[x+dx][y+dy]!="#" and visited[x+dx][y+dy]==-1:
#             visited[x+dx][y+dy]=visited[x][y]+1
#             queue.append([x+dx,y+dy])
