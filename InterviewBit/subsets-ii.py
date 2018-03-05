# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/subsets-ii/
# 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        subsets = set([()])

        for num in A:
            new = []
            for subset in subsets:
                new.append(subset + (num,))
                
            subsets.update(new)
            
        return sorted([list(s) for s in subsets])
        
