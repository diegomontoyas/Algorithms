# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/max-rectangle-in-binary-matrix/
# 

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if not A or not A[0]: return 0
        
        #Number of consecutive 1's to the right and including (i,j)
        memo = [[0]*len(A[0]) for _ in xrange(len(A))]
        
        #Precalculate memo
        for i in xrange(len(A)):
            count = 0
            for j in reversed(xrange(len(A[0]))):
                if A[i][j] == 1: count += 1
                else: count = 0
                memo[i][j] = count
        
        maxSize = 0
        
        #Start rectangles from every possible column
        for j in xrange(len(A[0])):
            
            #Start rectangles from every possible row
            for i in xrange(len(A)):
                #Height of the current sub-rectangle
                height = 0
                
                #Min width until some column is no longer 1
                minWidth = float("inf")

                #Enlarge rectangle downward until we find a 0 in the starting column.
                for i2 in xrange(i, len(A)):
                    if memo[i2][j] == 0: break
                    
                    height += 1
                    minWidth = min(minWidth, memo[i2][j])
                    
                    #Find out if the largest area has changed with the new height and even considering
                    #that the min width may be smaller than before
                    maxSize = max(maxSize, minWidth * height)
                
        return maxSize
                
                
