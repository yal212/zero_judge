from sys import stdin
input = stdin.readline
H, W, N = map(int, input().split())
for _ in range(N):
    m = [[0]*W]*H
    r, c, t, x = map(int, input().split())
