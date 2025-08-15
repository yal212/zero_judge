from sys import stdin
input = stdin.readline
M, N, j = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

def boom(Map, j, r, c, rad):
    