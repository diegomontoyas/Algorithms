# https://www.interviewbit.com/courses/programming/topics/trees/problems/sorted-array-to-balanced-bst/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A) == 0: return None
        return self.addArray(A, None)
        
    def addArray(self, array, root):
        if len(array) == 0: return root

        middle = len(array) / 2
        root = self.add(array[middle], root)
        root = self.addArray(array[:middle], root)
        root = self.addArray(array[middle+1:], root)
        return root
    
    def add(self, elem, root):
        if root is None: return TreeNode(elem)
        
        current = root
        added = False
        while not added:
            if elem < current.val:
                if current.left is None:
                    current.left = TreeNode(elem)
                    added = True
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(elem)
                    added = True
                else:
                    current = current.right
                    
        return root
            
