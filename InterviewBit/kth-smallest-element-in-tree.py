# https://www.interviewbit.com/courses/programming/topics/trees/problems/kth-smallest-element-in-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Integer:
    def __init__(self, val):
        self.val = val

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        return self._kthsmallest(root, Integer(k))
        
    def _kthsmallest(self, root, left):
        if root is None: return -1
        
        kthSmallest = self._kthsmallest(root.left, left)
        if kthSmallest != -1: return kthSmallest
        
        if left.val == 1:
            return root.val
        else:
            left.val -=1
        
        kthSmallest = self._kthsmallest(root.right, left)
        if kthSmallest != -1: return kthSmallest
        
        return -1


