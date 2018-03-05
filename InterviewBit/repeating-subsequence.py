# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/repeating-subsequence/
# 

class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        
        for i in xrange(len(A)):
            chars = {}
            foundRep = False
            
            for j in xrange(i+1, len(A)):
                if A[j] == A[i]: 
                    foundRep = True
                    
                if foundRep and A[j] in chars:
                    return True
                else:
                    chars[A[j]] = True
                    
        return False
                
