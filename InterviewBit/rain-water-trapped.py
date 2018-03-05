# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/rain-water-trapped/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        trappedWater = 0
        stack = []

        for i, level in enumerate(A):
            if i == 0: continue
            prevLevel = A[i - 1]

            if level < prevLevel:
                for _ in xrange(prevLevel - level):
                    stack.append(i)

            elif level > prevLevel:
                for _ in xrange(level-prevLevel):
                    if stack: trappedWater += (i - stack.pop())

        return trappedWater
        
