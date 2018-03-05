# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/simplify-directory-path/
# 

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        result = ""
        components = A.split("/")
        
        if not components: 
            return A
        
        stack = components[:1]
        
        for comp in components[1:]:
            if comp == ".." and len(stack)>1:
                stack.pop()
            elif comp not in ["", ".", ".."]:
                stack.append(comp)
                
        while stack:
            result += stack[0] + ("/" if len(stack) > 1 or len(result)==0 else "")
            del stack[0]
        
        return result
        
