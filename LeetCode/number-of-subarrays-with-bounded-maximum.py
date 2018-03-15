# https://leetcode.com/problems/count-of-smaller-numbers-after-self
# 84 ms
# O(|A|^2)

class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        
        total_sum = 0
        
        for i in range(len(A)):
            current_max = A[i]
            
            j=i
            while j<len(A) and current_max <= R:
                
                if current_max >= L:
                    total_sum += 1
                    
                j+=1
                if j<len(A): 
                    current_max = max(A[j] , current_max)
                
        return total_sum
