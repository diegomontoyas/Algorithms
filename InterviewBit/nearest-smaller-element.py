# https://www.interviewbit.com/problems/nearest-smaller-element/

from collections import deque

class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        
        numStack = deque()
        indexStack = deque()
        result = [-1]*len(arr)
        
        for i in reversed(range(len(arr))):
            num = arr[i]
            
            while self.top(numStack) > num:
                numStack.pop()
                poppedIndex = indexStack.pop()
                result[poppedIndex] = num
            
            numStack.append(num)
            indexStack.append(i)
            
        return result
            
    def top(self, queue):
        return queue[-1] if len(queue) != 0 else -1

