# NA (score:20%)
from sys import stdin
input = stdin.readline
M, N, j = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
start = None
for r, row in enumerate(Map):
    for c, val in enumerate(row):
        if val == -2:
            start = (r, c)
            break
    if start:
        break


def boom(Map, pos, rad):
    # M, N = len(Map), len(Map[0])
    r, c = pos
    squares = set()
    squares.add((r, c))
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for step in range(1, rad+1):
            nr, nc = r + dr*step, c + dc*step
            if not (0 <= nr < M and 0 <= nc < N):
                break
            if Map[nr][nc] == -1:
                break
            squares.add((nr, nc))

    return list(squares)


area = 0
rad = 1
while area < j:
    area = 1
    queue = [start]
    visited = {start}
    while queue:
        pos = queue.pop(0)
        if pos == start:
            radius = rad
        else:
            radius = Map[pos[0]][pos[1]]
        squares = boom(Map, pos, radius)
        for square in squares:
            if square not in visited:
                queue.append(square)
                visited.add(square)
                area += 1
    if area < j:
        rad += 1
print(rad)


# NA (score:20%)
from sys import stdin
input = stdin.readline
M, N, J = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    for j in range(N):
        if data[i][j] == -2:
            start = (i, j)

rad = 0

while True:
    queue = [(start[0], start[1], rad)]
    visited = {start: rad}
    while queue:
        x, y, r = queue.pop(0)
        if r == 0:
            continue
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if data[nx][ny] == -1:
                    continue
                nr = r - 1
                if data[nx][ny] > 0 and data[nx][ny] > nr:
                    nr = data[nx][ny]
                if (nx, ny) not in visited or nr > visited[(nx, ny)]:
                    visited[(nx, ny)] = nr
                    queue.append((nx, ny, nr))
    if len(visited) < J:
        rad += 1
    else:
        print(rad)
        break


# cheat 95% 
#0: 5% WA (line:1)
# 您的答案為: None
# 正確答案為: 2

def ANS(sr,sc,maze):
    visited,distance,queue={(sr,sc)},defaultdict(list),deque([(sr,sc,0)])#初始走訪過、距離、BFS queue
    while queue:#計算距離
        sr,sc,r=queue.popleft()
        visited.add((sr,sc))
        distance[r].append((sr,sc))
        for cr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=sr+cr,sc+cc
            if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and maze[nr][nc]>-1:
                visited.add((nr,nc))
                queue.append((nr,nc,r+1))
    visited={(sr,sc):0}#初始化引爆該格炸彈曾經的最大半徑
    for ans in range(1,max(distance)+1):#窮舉答案
        bomb=deque(distance[ans])#取出達到測試半徑可以多引爆的炸彈
        while bomb:#每個點查看
            queue=deque()
            sr,sc=bomb.popleft()
            queue.append((sr,sc,maze[sr][sc]))
            while queue:#BFS
                sr,sc,r=queue.popleft()
                if ((sr,sc) not in visited or visited[(sr,sc)]<r) and r>=0:
                    visited[(sr,sc)]=r#記錄引爆該格最大半徑
                    if r>0:
                        for cr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc=sr+cr,sc+cc
                            if 0<=nr<row and 0<=nc<col and maze[nr][nc]>-1:
                                queue.append((nr,nc,r-1))
                                if maze[nr][nc]>0:bomb.append((nr,nc))#半徑>=，1可以繼續連鎖反應
        if len(visited)>=q:return ans#引爆q個
from collections import deque,defaultdict
row,col,q=map(int,input().split())
maze=[]
for r in range(row):
    line=list(map(int,input().split()))
    if -2 in set(line):sr,sc=r,line.index(-2)
    maze.append(line)
print(ANS(sr,sc,maze))