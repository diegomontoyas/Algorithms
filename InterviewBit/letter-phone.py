# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/letter-phone/
# 

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        if len(A) == 0: return []
        
        map = {"1":"1","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno", \
                "7":"pqrs","8":"tuv","9":"wxyz","0":"0"}
        
        if len(A) == 1:
            return list(map[A[0]])
        
        result = []
        letters = map[A[0]]
        combinations = self.letterCombinations(A[1:])
        
        for letter in letters:
            result += [letter + comb for comb in combinations] 
            
        return result
        
