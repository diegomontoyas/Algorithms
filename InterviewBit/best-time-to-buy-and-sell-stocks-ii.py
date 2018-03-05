# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/best-time-to-buy-and-sell-stocks-ii/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0
        boughtStock = False

        for i in xrange(len(A)):
            if not boughtStock and (i==0 or A[i-1] >= A[i]) and i<len(A)-1 and A[i+1] >= A[i]:
                #We are at a low, so we buy
                profit -= A[i]
                boughtStock = True
                
            elif boughtStock and i>0 and A[i-1] <= A[i] and (i==len(A)-1 or A[i] >= A[i+1]):
                #We are at a peak, so we sell
                profit += A[i] 
                boughtStock = False
        
        return profit
        
