from sys import stdin
input = stdin.readline

while True:
    try:
        n = int(input())
        print(1 + n * (n - 1) // 2)
    except:
        break