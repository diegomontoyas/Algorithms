# https://www.interviewbit.com/courses/programming/topics/trees/problems/next-greater-number-bst/
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
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        node = self.find(A, B)

        if node.right:
            return self.findMin(node.right)
        else:
            successor = None
            current = A

            while current.val != B:
                if current.val > B:
                    successor = current 
                    current = current.left
                else:
                    current = current.right
            
            return successor
        
    def findMin(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def find(self, root, data):
        current = root
        
        while current.val != data:
            if data < current.val:
                current = current.left
            else:
                current = current.right
    
        return current
            

