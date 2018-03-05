# https://www.interviewbit.com/courses/programming/topics/trees/problems/construct-binary-tree-from-inorder-and-preorder/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        
        root = TreeNode(preorder[0])
        inorderRootIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1 + inorderRootIndex], inorder[:inorderRootIndex])
        root.right = self.buildTree(preorder[1 + inorderRootIndex:], inorder[inorderRootIndex + 1:])
        
        return root
        
