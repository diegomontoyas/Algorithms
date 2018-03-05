# https://www.interviewbit.com/courses/programming/topics/hashing/problems/diffk-ii/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        hashTable = {}
        
        for i, ele in enumerate(A):
            if ele in hashTable:
                hashTable[ele].append(i)
            else:
                hashTable[ele] = [i]
            
        for ele in A:
            if B+ele in hashTable:
                if B != 0 or len(hashTable[B+ele]) >= 2:
                    return True
                    
        return False
        
