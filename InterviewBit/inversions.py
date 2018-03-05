# https://www.interviewbit.com/courses/programming/topics/heaps-and-maps/problems/inversions/
# 

class Integer:
    def __init__(self):
        self.val = 0
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        counter = Integer()
        self.mergeSort(A, counter)
        return counter.val
        
    def mergeSort(self, A, counter):
        if len(A) == 1: return A
        
        half = len(A)/2
        firstHalf = self.mergeSort(A[0:half], counter)
        secondHalf = self.mergeSort(A[half:], counter)
        return self.merge(firstHalf, secondHalf, counter)
        
    def merge(self, A, B, counter):
        newList = []
        
        i,j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                newList.append(A[i])
                i+=1
            else:
                newList.append(B[j])
                j+=1
                counter.val += len(A)-i
        
        newList.extend(A[i:])
        newList.extend(B[j:])
        return newList

