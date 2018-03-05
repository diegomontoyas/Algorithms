# https://www.interviewbit.com/courses/programming/topics/trees/problems/inorder-traversal/
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
    def inorderTraversal(self, A):
        added = {}
        result = []
        stack = [A]
        
        while stack:
            node = stack[len(stack)-1]

            if node.left and node.left.val not in added:
                stack.append(node.left)
                
            elif node.val not in added:
                result.append(node.val)
                added[node.val] = True
                stack.pop()
                
                if node.right:
                    stack.append(node.right)
                
        return result
                
