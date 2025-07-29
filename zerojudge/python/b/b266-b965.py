# once = False
# while True:
#     try:
#         if once:
#             print("\n")
#         line = input()
#         if not line.strip():
#             break
#         row, col, m = map(int, line.split())
#         array = [list(map(int, input().split())) for _ in range(row)]
#         operaters = map(int, input().split())
#         for op in operaters:
#             c = len(array[0])
#             r = len(array)
#             if op == 0:
#                 temp = [[0] * r for _ in range(c)]
#                 for i in range(c):
#                     for j in range(r):
#                         temp[i][j] = array[r-j-1][i]
#             else:
#                 temp = [[0] * c for _ in range(r)]
#                 for i in range(r):
#                     for j in range(c):
#                         temp[i][j] = array[r-i-1][j]
#             array = temp
#         c = len(array[0])
#         r = len(array)
#         print(r, c)
#         for rs in array:
#             print(*rs)
#         once = True
#     except:
#         break

# :(

while True:
    try:
        line = input()
        if not line.strip():
            break
        row, col, m = map(int, line.split())
        array = [list(map(int, input().split())) for _ in range(row)]
        operaters = list(map(int, input().split()))  # convert to list

        for op in reversed(operaters):  # loop from last to first
            c = len(array[0])
            r = len(array)
            if op == 0:
                # Rotate 90° counterclockwise
                temp = [[0] * r for _ in range(c)]
                for i in range(c):
                    for j in range(r):
                        temp[i][j] = array[j][c - 1 - i]
            else:
                # Flip vertically
                temp = [[0] * c for _ in range(r)]
                for i in range(r):
                    for j in range(c):
                        temp[i][j] = array[r - 1 - i][j]
            array = temp

        c = len(array[0])
        r = len(array)
        print(r, c)
        for row in array:
            print(*row)
    except:
        break
