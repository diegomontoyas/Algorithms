# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/kth-permutation-sequence/
# 

class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        import math
        if not (1 <= k <= math.factorial(n)): return ""
        numbers = [x for x in xrange(1, n + 1)]
        result = ""
    
        lastGroup = 1
        i = 0
        while i < n - 1:
            countByGroup = math.factorial(x-1-i)
            k -= (lastGroup - 1) * math.factorial(x-i)
            group = int(math.ceil(float(k) / countByGroup))
            lastGroup = group
            result += str(numbers.pop(group - 1))
            i += 1
    
        result += str(numbers.pop(0))
        return result
        
