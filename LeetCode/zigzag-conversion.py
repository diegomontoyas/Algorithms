# https://leetcode.com/problems/zigzag-conversion/
# 100ms

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        from collections import deque
        
        if numRows <= 1 or numRows >= len(s):
            return s
        
        resultRows = [deque() for _ in range(numRows)]
        row = 0
        downward = True
        
        for char in s:
            resultRows[row].append(char)
            
            if row == numRows-1: 
                downward = False
            elif row == 0:
                downward = True
            
            if downward:
                row += 1
            else:
                row -= 1
                
        resultDeque = deque()
        for deque in resultRows:
            resultDeque.extend(deque)
            
        return ''.join(resultDeque)
        
