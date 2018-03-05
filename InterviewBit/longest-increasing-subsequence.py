# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/longest-increasing-subsequence/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        #longest ending in i
        longest = 0
        mem = []
        
        for i in xrange(len(A)):
            prevLongest = None
            
            for j in xrange(i):
                if A[j] < A[i] and mem[j] > prevLongest:
                    prevLongest = mem[j]
                
            if prevLongest is None:
                mem.append(1)
            else:
                mem.append(prevLongest+1)
                
            longest = max(mem[-1], longest)
            
        return longest
        
