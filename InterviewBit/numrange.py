# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/numrange/
# 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        if not A: return 0
        
        i,j = 0,1
        currentSum = A[0]
        n = 0
        
        while i < len(A):
            
            if B <= currentSum <= C:
                n += 1
                
                j+=1
                if j <= len(A):
                    currentSum += A[j-1]
                else:
                    i+=1
                    j=i+1
                    
                    if i<len(A):
                        currentSum = A[i]
                
            elif currentSum > C:
                i+=1
                j=i+1
                
                if i<len(A):
                    currentSum = A[i]
            else:
                j+=1
                if j <= len(A):
                    currentSum += A[j-1]
                else:
                    i+=1
                    j=i+1
                    
                    if i<len(A):
                        currentSum = A[i]
                        
        return n
                
                
