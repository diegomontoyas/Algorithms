# https://www.interviewbit.com/courses/programming/topics/trees/problems/path-sum/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A: return False
        
        if not (A.left or A.right):
            return A.val == B
            
        return self.hasPathSum(A.left, B-A.val) or self.hasPathSum(A.right, B-A.val)
        
