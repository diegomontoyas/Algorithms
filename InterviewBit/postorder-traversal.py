# https://www.interviewbit.com/courses/programming/topics/trees/problems/postorder-traversal/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        result = []
        stack = [A]
        added = set()
        
        while stack:
            top = stack[-1]
            
            if top.left and top.left.val not in added:
                stack.append(top.left)
            elif top.right and top.right.val not in added:
                stack.append(top.right)
            else:
                stack.pop()
                result.append(top.val)
                added.add(top.val)
                
        return result
        
        
