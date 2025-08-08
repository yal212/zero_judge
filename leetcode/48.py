class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        temp = [[-1 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                temp[j][l-1-i] = matrix[i][j]
        for i in range(l):
            for j in range(l):
                matrix[i][j] = temp[i][j]
