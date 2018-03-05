# https://www.interviewbit.com/courses/programming/topics/trees/problems/binary-tree-from-inorder-and-postorder/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if not inorder: return

        rootVal = postorder[-1]
        root = TreeNode(rootVal)

        inorderRootIndex = inorder.index(rootVal)

        leftInorder = inorder[:inorderRootIndex]
        rightInorder = inorder[inorderRootIndex + 1:]

        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):-1]

        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        return root
        
        
