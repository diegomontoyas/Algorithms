# https://www.interviewbit.com/courses/programming/topics/trees/problems/preorder-traversal/
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
    def preorderTraversal(self, A):
        result = []
        stack = [A]
        
        while stack:
            top = stack.pop()
            result.append(top.val)
            
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)

        return result            
            
