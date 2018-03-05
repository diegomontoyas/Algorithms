# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/combinations/
# 

class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        result = []
        self.recurse(k, n, 1, [], result)
        return result
        
    def recurse(self, k, n, level, path, result):
        if level > k:
            result.append(path)
            return
        
        parent = path[-1] if path else 0
        for num in xrange(parent+1, n-k+level +1):
            self.recurse(k, n, level+1, path+[num], result)
        
