# https://www.interviewbit.com/courses/programming/topics/arrays/problems/kth-row-of-pascals-triangle/
# 

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        lastLevel = [1]
        
        for level in xrange(1, A+1):
            newNums = []
            
            for i in xrange(level+1):
                topLeft = lastLevel[i-1] if i>0 else 0
                topRight = lastLevel[i] if i<len(lastLevel) else 0
                newNums.append(topLeft+topRight)
            lastLevel = newNums
            
        return lastLevel
