# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/all-unique-permutations/
# 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        A.sort()
        return self.permutations(A)
        
    def permutations(self, A):
        if len(A) == 1:
            return [A]
            
        result = []
        for i, elem in enumerate(A):
            if i==0 or A[i-1] != elem:
                permutations = self.permutations(A[:i] + A[i+1:])
                result.extend([[elem] + perm for perm in permutations])
            
        return result 
        
