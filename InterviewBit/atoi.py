# https://www.interviewbit.com/courses/programming/topics/strings/problems/atoi/
# 

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        if len(A) == 0: return 0
        
        charToNumDic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        result = 0
        negative = False
        
        i=0
        while i<len(A)-1 and A[i] == " ":
            i+=1
            
        if A[i] == "-":
            negative = True
            i+=1
        elif A[i] == "+":
            i+=1
        elif A[i] not in charToNumDic: 
            return 0
        
        while i<len(A) and A[i] in charToNumDic:
            num = charToNumDic[A[i]]
            result += num*(10**(len(A)-i-1))
            i+=1
        
        return min(result, 2147483647) if not negative else max(-result, -2147483648)
                
        
