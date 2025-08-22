from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

def man(p1, p2):
    a, b, c, d = p1[0], p1[1], p2[0], p2[1]
    return abs(a-c) + abs(b-d)