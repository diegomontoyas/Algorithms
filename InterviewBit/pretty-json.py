# https://www.interviewbit.com/courses/programming/topics/strings/problems/pretty-json/
# 

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        result = []
        indentLevel = 0
        wordBeginning = None
        
        for i, char in enumerate(A):
            if char == " ": 
                continue
            
            elif char in ["[", "{"]:
                nextCharComma = i<len(A)-1 and A[i+1] == ","
                result.append("\t"*indentLevel + char + ("," if nextCharComma else ""))
                indentLevel += 1
                
            elif char in ["]", "}"]:
                indentLevel -= 1
                nextCharComma = i<len(A)-1 and A[i+1] == ","
                result.append("\t"*indentLevel + char + ("," if nextCharComma else ""))
            
            elif wordBeginning == None and char != ",":
                wordBeginning = i 

            if wordBeginning != None and (
                char == ","
                or (i<len(A)-1 and A[i+1] in ["]", "}"])
                or (char == ":" and i<len(A) and A[i+1] in ["[", "{"]) ):
                    
                    result.append("\t"*indentLevel + A[wordBeginning:i+1])
                    wordBeginning = None
                
        return result
        
