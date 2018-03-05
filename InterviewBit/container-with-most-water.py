# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/container-with-most-water/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        maxWater = 0
        
        i,j = 0, len(A)-1
        while i<j:
            shortestPole = min(A[i], A[j])
            maxWater = max(maxWater, (j-i)*shortestPole) 
            
            if A[i] == shortestPole:
                i+=1
            else:
                j-=1
                
        return maxWater
