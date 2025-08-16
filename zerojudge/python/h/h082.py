from sys import stdin
input = stdin.readline
n, m = int(input())
temp = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
players = [[] for _ in range(n)]
for i, player in enumerate(temp):
    players[order[i]] = player
