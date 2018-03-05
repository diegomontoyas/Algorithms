# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/3-sum/
# 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        target = B
        bestSum = None
    
        i = 0
        while i<len(A):
            j,k = i+1,len(A)-1
            
            while j < k:
                sum = A[i]+A[j]+A[k]
                
                if not (i == j == k) and (bestSum == None or abs(sum - target) < abs(bestSum - target)):
                    bestSum = sum
                    if bestSum == target: return bestSum
                    
                elif sum > target:
                    k-=1
                else:
                    j+=1
            i+=1
    
        return bestSum
                    
            
