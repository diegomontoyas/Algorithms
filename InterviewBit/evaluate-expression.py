# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/evaluate-expression/
# 

class Solution:
    
    def eval(self, s):
        num1 = int(s[0])
        num2 = int(s[1])
        op = s[2]
        
        if op == "*": return num1 * num2
        elif op == "-": return num1-num2
        elif op == "+": return num1+num2
        else: return num1/num2
            
    def isOp(self, s):
        if len(s)<3: return False
        return s[0].replace('-', '').isdigit() and s[1].replace('-', '').isdigit() and s[2] in ["*","/","+","-"]

    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        
        while len(A) != 1:
            i=0
            while i<len(A):
                s = A[i:i+3]
                if self.isOp(s):
                    result = self.eval(s)
                    del A[i:i+3]
                    A.insert(i, str(result))
                
                i+=1
        
        return A[0] 
            
        
