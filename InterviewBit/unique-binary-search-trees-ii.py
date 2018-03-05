# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/unique-binary-search-trees-ii/
# 

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        return self._numTrees(A, {})

    def _numTrees(self, num, memo):
        if num <= 1: return 1
        if num in memo: return memo[num]
        
        total = 0
        for n in xrange(1, num+1):
            leftWays = self._numTrees(n - 1, memo)
            rightWays = self._numTrees(num - n, memo)
            total += leftWays * rightWays
            
        memo[num] = total        
        return total
