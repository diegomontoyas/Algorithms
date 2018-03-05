# https://www.interviewbit.com/courses/programming/topics/greedy/problems/majority-element/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        dic = {}
        
        for elem in A:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
                
            if dic[elem] > len(A)/2:
                return elem
        
