# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/permutations/
# 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1:
            return [A]
            
        result = []
        A.sort()
        for i, elem in enumerate(A):
            permutations = self.permute(A[:i] + A[i+1:])
            result.extend([[elem] + perm for perm in permutations])
            
        return result 
