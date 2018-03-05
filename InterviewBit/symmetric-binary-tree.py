# https://www.interviewbit.com/courses/programming/topics/trees/problems/symmetric-binary-tree/
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
    def isSymmetric(self, A):
        if not A: return
        return self.areSymmetric(A.left, A.right)
        
    def areSymmetric(self, root1, root2):
        if not (root1 or root2):
            return True
        if not (root1 and root2):
            return False
        if root1.val != root2.val:
            return False
        if not self.areSymmetric(root1.left, root2.right):
            return False
        if not self.areSymmetric(root1.right, root2.left):
            return False
            
        return True
    
