# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/max-sum-path-in-binary-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Integer:
    def __init__(self, x):
        self.val = x

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        if not A: return -2147483648
        
        memoTree = self.populateMemoTree(A)
        maxSum = Integer(float("-inf"))
        self.findMaxPath(A, memoTree, maxSum)
        return maxSum.val
        
    def findMaxPath(self, root, memoRoot, maxSoFar):
        if not root: return
        
        leftAndRight = [n.val for n in [memoRoot.left, memoRoot.right] if n is not None]
        maxSoFar.val = max(maxSoFar.val, sum(leftAndRight + [0]) + root.val, root.val)
        
        self.findMaxPath(root.left, memoRoot.left, maxSoFar)
        self.findMaxPath(root.right, memoRoot.right, maxSoFar)

    def populateMemoTree(self, root):
        if not root: return
        
        newRoot = TreeNode(root.val)
        newRoot.left = self.populateMemoTree(root.left)
        newRoot.right = self.populateMemoTree(root.right)
        
        vals = [v.val for v in [newRoot.left, newRoot.right] if v is not None and v.val > 0]
        if vals: newRoot.val = max(vals) + root.val

        return newRoot
        
        
