# https://www.interviewbit.com/courses/programming/topics/trees/problems/inorder-traversal-of-cartesian-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A) == 0: return None
        
        if len(A) == 1: 
            return TreeNode(A[0])
        
        maxIndex = max(xrange(len(A)), key=A.__getitem__)
        maxVal = A[maxIndex]
        
        leftBranch = self.buildTree(A[:maxIndex])
        rightBranch = self.buildTree(A[maxIndex+1:])
        
        root = TreeNode(maxVal)
        root.left = leftBranch
        root.right = rightBranch
        
        return root
        
