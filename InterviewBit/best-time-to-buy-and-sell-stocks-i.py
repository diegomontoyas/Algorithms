# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/best-time-to-buy-and-sell-stocks-i/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        maxProfit = 0
        maxsToRight = []
        
        for num in reversed(A):
            if not maxsToRight or num >= maxsToRight[-1]:
                maxsToRight.append(num)
        
        for i in xrange(len(A)):
            maxToRight = maxsToRight[-1]
            if maxToRight == A[i]: maxsToRight.pop()
            maxProfit = max(maxProfit, maxToRight-A[i])
            
        return maxProfit
