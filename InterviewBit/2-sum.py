# https://www.interviewbit.com/courses/programming/topics/hashing/problems/2-sum/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        map = {}
        
        for i, num in enumerate(A):
            if B-num in map:
                leftIndex = map[B-num]
                return [leftIndex+1, i+1]
            if num not in map:
                map[num] = i

        return []
        
