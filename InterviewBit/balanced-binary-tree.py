# https://www.interviewbit.com/courses/programming/topics/trees/problems/balanced-binary-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if not A: return True
        return self._isBalanced(A) is not None

    def _isBalanced(self, A):
        if not A: return 0
        if not (A.left or A.right): return 1
        
        leftH = self._isBalanced(A.left)
        rightH = self._isBalanced(A.right) 
        isBalanced = leftH is not None and rightH is not None and abs(leftH - rightH) <= 1
        
        return max(leftH, rightH) + 1 if isBalanced else None
        
        
