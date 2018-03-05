# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/stairs/
# 

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        return self.posibilities({}, A)
        
    def posibilities(self, memory, n):
        if n <= 1: return 1
        if n in memory: return memory[n]
        memory[n] = self.posibilities(memory, n-1) + self.posibilities(memory, n-2)
        return memory[n]
