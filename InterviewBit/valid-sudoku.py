# https://www.interviewbit.com/courses/programming/topics/hashing/problems/valid-sudoku/
# 

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        
        def valid(cell, nums):
            if cell != ".":
                if cell in nums:
                    return False
                else:
                    nums[cell] = 1
            return True
        
        # Rows
        for row in A:
            nums = {}
            for cell in row:
                if not valid(cell, nums): return 0
                
        # Columns
        for j in xrange(len(A[0])):
            nums = {}
            for i in xrange(len(A)):
                if not valid(A[i][j], nums): return 0
                
        # Squares
        for dx in xrange(3):
            for dy in xrange(3):
                nums = {}
                for i in xrange(3):
                    for j in xrange(3):
                        if not valid(A[i+dx*3][j+dy*3], nums): return 0
        
        return 1        
                
                
                    

