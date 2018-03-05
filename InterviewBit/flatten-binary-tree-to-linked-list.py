# https://www.interviewbit.com/courses/programming/topics/trees/problems/flatten-binary-tree-to-linked-list/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        root = TreeNode("dummy")
        root.left = A
        rightEnd = root
        
        while root.left is not None:
            toMove = root.left
            
            if toMove.right is not None:
                rightMost = self.rightMost(toMove.left)
                
                if rightMost is not None:
                    rightMost.right = toMove.right
                elif toMove.left is not None:
                    toMove.left.right = toMove.right
                else:
                    toMove.left = toMove.right

            root.left = toMove.left
            rightEnd.right = toMove
            rightEnd = toMove
            toMove.right = None
            toMove.left = None
            
        return root.right
        
    def rightMost(self, root):
        firstWithRight = None
        current = root
        
        while current is not None and firstWithRight is None:
            if current.right is not None:
                firstWithRight = current
            else:
                current = current.left
        
        if current is not None:
            while current.right is not None:
                current = current.right    

        return current
    
        
        
        
        
