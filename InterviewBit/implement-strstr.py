# https://www.interviewbit.com/courses/programming/topics/strings/problems/implement-strstr/
# 

class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        
        if len(haystack) == 0 or len(needle) == 0:
            return -1
            
        i=0
        while i+len(needle)-1 < len(haystack):
            
            j=0
            while j < len(needle):
                if haystack[i+j] != needle[j]: 
                    break
                elif j == len(needle)-1:
                    return i
                else:
                    j+=1
            
            i+=1
            
        return -1
        
