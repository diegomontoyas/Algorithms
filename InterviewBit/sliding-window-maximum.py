# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/sliding-window-maximum/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if B == 0: return []
        if B >= len(A): return [max(A)]
        
        from collections import deque
        result = []
        maxDeque = deque()

        for i in xrange(len(A)+1):
            removed = A[i-B] if i-B >= 0 else None
            new = A[i] if i<len(A) else None

            if removed is not None:
                result.append(maxDeque[0])

                if removed == maxDeque[0]:
                    maxDeque.popleft()

            if new is not None:
                if not maxDeque:
                    maxDeque.append(new)
                else:
                    while maxDeque and maxDeque[-1] < new:
                        maxDeque.pop()
                    maxDeque.append(new)

        return result
                
                
