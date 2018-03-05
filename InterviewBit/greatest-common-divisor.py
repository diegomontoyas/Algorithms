# https://www.interviewbit.com/courses/programming/topics/math/problems/greatest-common-divisor/
# 

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A==0 or B==0: return max(A, B)
        for div in reversed(xrange(1, min(A,B)+1)):
            if A % div == 0 and B % div == 0:
                return div
