# https://www.interviewbit.com/courses/programming/topics/trees/problems/sum-root-to-leaf-numbers/
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
    def sumNumbers(self, A):
        sum = Integer(0)
        self.sumRootToLeaves(A, sum, [])
        return sum.val % 1003
        
    def sumRootToLeaves(self, root, sum, currentPath):
        if not root: return
    
        currentPath.append(root.val)
        
        if not (root.left or root.right):
            sum.val += int(''.join(map(str, currentPath)))
            
        self.sumRootToLeaves(root.left, sum, currentPath)
        self.sumRootToLeaves(root.right, sum, currentPath)
        
        del currentPath[-1]
        
