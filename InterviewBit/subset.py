# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/subset/
# 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        result = [[]]
        for x in A:
            result.extend([sorted(subset + [x]) for subset in result])
        return sorted(result)
