# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/ways-to-decode/
# 

class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        for i, char in enumerate(A):
            if char == "0" and (i==0 or A[i-1] not in ["1", "2"]):
                return 0
        
        return self._numDecodings(A, {})

    def _numDecodings(self, A, mem):
        if A in mem: 
            return mem[A]
            
        if len(A)==1:
            return 1 if A != "0" else 0
        
        if len(A)==2:
            num = int(A)
            if 10 <= num <= 26 and 10 != num != 20: return 2
            else: return 1

        oneChar, twoChars = 0, 0

        if A[1] != "0":
            oneChar = self._numDecodings(A[1:], mem)
            
            if 10 <= int(A[:2]) <= 26:
                twoChars = self._numDecodings(A[2:], mem)
            
        mem[A] = oneChar + twoChars
        return mem[A]
        
