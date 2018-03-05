# https://www.interviewbit.com/courses/programming/topics/hashing/problems/colorful-number/
# 

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        explored = {}
        
        for partSize in xrange(1, len(A)+1):
            for i in xrange(len(A)+1-partSize):
                partition = A[i:i+partSize]
                
                prod = 1
                for s in partition:
                    prod *= int(s)
                    
                if prod in explored:
                    return 0
                
                explored[prod] = 1
                    
        return 1
            
