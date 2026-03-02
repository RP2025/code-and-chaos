class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = [0] * len(matrix)
        zero_col = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row[i],zero_col[j] = 1,1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zero_row[i] or zero_col[j]:
                    matrix[i][j] = 0
                

        
        