# https://www.interviewbit.com/courses/programming/topics/strings/problems/longest-common-prefix/
# 

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A: return ""
        
        prefix = ""
        i = 0
        
        while True:
            newLetter = None
            
            for string in A:
                if i >= len(string):
                    return prefix
                
                if newLetter is None:
                    newLetter = string[i]
                elif string[i] != newLetter:
                    return prefix
            
            i += 1
            prefix += newLetter
            
