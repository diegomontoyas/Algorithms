# https://www.interviewbit.com/courses/programming/topics/arrays/problems/pascal-triangle/
# 

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0: return []
        
        triangle = [[1]]
        for level in xrange(2, A+1):
            lastLevel = triangle[-1]
            newNums = []
            
            for i in xrange(level):
                topLeft = lastLevel[i-1] if i>0 else 0
                topRight = lastLevel[i] if i<len(lastLevel) else 0
                newNums.append(topLeft+topRight)
            
            triangle.append(newNums)
            
        return triangle
