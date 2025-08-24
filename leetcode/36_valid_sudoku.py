class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cur = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] not in cur:
                    cur.add(board[i][j])
                elif board[i][j] in cur:
                    return False
        for i in range(9):
            cur = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] not in cur:
                    cur.add(board[j][i])
                elif board[j][i] in cur:
                    return False
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                cur = set()
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    now = board[i+dx][j+dy]
                    if now != "." and now not in cur:
                        cur.add(now)
                    elif now in cur:
                        return False
        return True
