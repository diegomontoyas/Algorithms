# https://leetcode.com/problems/validate-binary-search-tree/
# 72 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root)[0]
    
    def _isValidBST(self, root):
        
        if root is None: return True, None, None
        
        val = root.val        
        leftIsBST, leftMin, leftMax = self._isValidBST(root.left)
        rightIsBST, rightMin, rightMax = self._isValidBST(root.right)
        
        newMin = min(leftOrRight(leftMin, val), leftOrRight(rightMin, val), val)
        newMax = max(leftOrRight(leftMax, val), leftOrRight(rightMax, val), val)

        leftMaxValid = leftMax is None or leftMax < val
        rightMinValid = rightMin is None or rightMin > val
        
        isBST = leftIsBST and rightIsBST and leftMaxValid and rightMinValid
        return isBST, newMin, newMax
    
def leftOrRight(s,d):
    return s if s is not None else d
