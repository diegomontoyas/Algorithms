# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/largest-rectangle-in-histogram/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        A.append(0)
        stack = []
        maxRect = 0
        
        for i, h in enumerate(A):
            if not stack or h > stack[-1][1]:
                stack.append((i,h))
            elif h < stack[-1][1]:
                while stack and h < stack[-1][1]:
                    si, sh = stack.pop()
                    maxRect = max(maxRect, (i-si) * sh)
                
                stack.append((si, h))
        
        return maxRect
            
