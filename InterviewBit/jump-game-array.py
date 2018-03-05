# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/jump-game-array/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 1: return True
        mem =  [None]*len(A)
        
        for i in reversed(xrange(len(A))):
            if A[i]==0:
                mem[i] = False
            elif A[i]>=len(A)-i:
                mem[i] = True
            else:
                j=i+1
                while j<len(A) and j-i<=A[i] and mem[i] is None:
                    if mem[j]: mem[i] = True
                    j+=1
                    
                if mem[i] is None: mem[i]=False
        
        return mem[0]
        
