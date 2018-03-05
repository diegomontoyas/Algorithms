# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/max-product-subarray/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        memo = []
        maxProd = None

        for num in A:
            memo.append((memo[-1] if memo and memo[-1] != 0 else 1) * num)

        for i in xrange(len(memo)):
            prod = memo[i]

            j=i-1
            while j>=0 and memo[j] != 0:
                j-=1

            for j in xrange(j+1,i+1):
                maxProd = max(maxProd, prod)
                if j != i:
                    prod /= memo[j] if memo[j] != 0 else 1

        return maxProd or 0
        
