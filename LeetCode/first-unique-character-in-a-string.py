# https://leetcode.com/problems/first-unique-character-in-a-string
# 232 ms

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map = {}
        
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
                
        for i, c in enumerate(s):
            if c in map and map[c] == 1:
                return i
        
        return -1
