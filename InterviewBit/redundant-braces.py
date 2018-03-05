# https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/redundant-braces/
# 

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        ops = ["+", "-", "/", "*"]

        for i, char in enumerate(A):
            if char == "(":
                stack.append(True)

            elif char == ")":
                if stack:
                    if stack[len(stack) - 1]:
                        return True
                    else:
                        stack.pop()

            elif char in ops:
                if stack:
                    stack[len(stack) - 1] = stack[len(stack) - 1] and False

        return False
                
