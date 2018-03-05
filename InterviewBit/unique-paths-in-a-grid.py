# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/unique-paths-in-a-grid/
# 

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        pathCounts = [[None]*len(A[0]) for _ in xrange(len(A))]
        
        for i in reversed(xrange(len(A))):
            for j in reversed(xrange(len(A[0]))):
                if A[i][j] == 1:
                    pathCounts[i][j] = 0
                    
                elif i != len(A)-1 and j != len(A[0])-1:
                    pathCounts[i][j] = pathCounts[i+1][j] + pathCounts[i][j+1]
                    
                elif i == len(A)-1 and j != len(A[0])-1:
                    pathCounts[i][j] = pathCounts[i][j+1]
                    
                elif i != len(A)-1 and j == len(A[0])-1:
                    pathCounts[i][j] = pathCounts[i+1][j]
                    
                else:
                    pathCounts[i][j] = 1
                    
        return pathCounts[0][0]
                    
    
                    
