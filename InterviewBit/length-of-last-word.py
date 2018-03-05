# https://www.interviewbit.com/courses/programming/topics/strings/problems/length-of-last-word/
# 

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        
        j=len(A)-1
        while j>=0 and A[j] == " ":
            j-=1
        
        if j<0: return 0
            
        i=j
        while i>=0 and A[i] != " ":
            i-=1
        
        return j-i
