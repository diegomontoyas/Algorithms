# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/min-sum-path-in-matrix/
# 

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A or not A[0]: return 0
        memo = [[None]*len(A[0]) for _ in xrange(len(A))]

        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if i == 0 and j == 0:
                    memo[i][j] = A[i][j]
                elif i == 0:
                    memo[i][j] = memo[i][j-1] + A[i][j]
                elif j == 0:
                    memo[i][j] = memo[i-1][j] + A[i][j]
                else:
                    memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + A[i][j]

        return memo[-1][-1]

