# https://www.interviewbit.com/courses/programming/topics/hashing/problems/4-sum/
# 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A.sort()
        s = set([A[0]])
        res = set()
        
        for i in xrange(len(A)-2):
            for j in xrange(i+1, len(A)-2):
                k,l = j+1, len(A)-1
                
                while k<l:
                    sum = A[i]+A[j]+A[l]+A[k]
                    
                    if sum == B:
                        res.add((A[i],A[j],A[k],A[l]))
                        k+=1
                        
                    elif sum > B:
                        l-=1
                    else:
                        k+=1
               
        res = sorted([list(x) for x in res])
        return res
                    
