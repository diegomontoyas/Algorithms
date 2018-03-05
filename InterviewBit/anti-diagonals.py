# https://www.interviewbit.com/courses/programming/topics/arrays/problems/anti-diagonals/
# 

class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        result = []

        for n in xrange(2):
            for i in xrange(0 if n == 0 else 1, len(a)):
                row = 0 if n == 0 else i
                col = i if n == 0 else len(a) - 1
                diagonal = []
    
                while col >= 0 and row < len(a):
                    diagonal.append(a[row][col])
                    col -= 1
                    row += 1
    
                result.append(diagonal)
    
        return result
        
