# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/sort-by-color/
# 

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        return self.mergeSort(A)
        
    def mergeSort(self, A):
        if len(A) == 1: return A
        
        half = len(A)/2
        firstHalf = self.mergeSort(A[0:half])
        secondHalf = self.mergeSort(A[half:])
        return self.merge(firstHalf, secondHalf)
        
    def merge(self, A, B):
        newList = []
        
        i,j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                newList.append(A[i])
                i+=1
            else:
                newList.append(B[j])
                j+=1
                    
        newList.extend(A[i:])
        newList.extend(B[j:])
        return newList
                
