# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/edit-distance/
# 

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        A, B = A.strip(), B.strip()
        memo = [[None]*(len(B)+1) for _ in xrange(len(A)+1)]
        return self._minDistance(A, B, memo)
        
    def _minDistance(self, A, B, memo):
        cached = memo[len(A)][len(B)]
        if cached: return cached
        if len(A) == len(B) == 0: return 0
        
        replace, insert, delete = None, None, None
        
        if len(A) > 0 and len(B) > 0:
            replace = self._minDistance(A[1:], B[1:], memo) + (1 if A[0] != B[0] else 0)
        if len(B) > 0:
            insert = self._minDistance(A, B[1:], memo) + 1
        if len(A) > 0:
            delete = self._minDistance(A[1:], B, memo) + 1

        res = min([n for n in replace, insert, delete if n is not None])
        memo[len(A)][len(B)] = res
        return res
        
