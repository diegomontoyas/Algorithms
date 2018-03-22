# https://leetcode.com/problems/toeplitz-matrix
# 56 ms

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        for row in range(len(matrix)):
            if not self.isValidDiagonal(matrix, row, 0):
                return False
            
        for col in range(1, len(matrix[0])):
            if not self.isValidDiagonal(matrix, 0, col):
                return False
            
        return True
            
    def isValidDiagonal(self, matrix, i, j):
        
        element = matrix[i][j]
        row, col = i, j
        
        while row<len(matrix) and col<len(matrix[row]):
            if matrix[row][col] != element:
                return False
            row+=1
            col+=1
            
        return True
