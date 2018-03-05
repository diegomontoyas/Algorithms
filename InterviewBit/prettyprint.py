# https://www.interviewbit.com/courses/programming/topics/arrays/problems/prettyprint/
# 

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = (A*2)-1
        result = [[0]*size for _ in xrange(size)]
        
        row = 0
        while row<size:
            col = 0
            while col<size:
                result[col][row] = max(abs(row-(A-1)), abs(col-(A-1))) + 1
                col += 1
            row += 1
        return result
