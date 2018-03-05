# https://www.interviewbit.com/courses/programming/topics/trees/problems/root-to-leaf-paths-with-sum/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        result = []
        self.findPaths(root, sum1, result, [])
        return result

    def findPaths(self, root, remaining, result, pathSoFar):
        if root is None: return
    
        pathSoFar.append(root.val)
        if root.left is None and root.right is None and remaining - root.val == 0:
            result.append(list(pathSoFar))

        self.findPaths(root.left, remaining - root.val, result, pathSoFar)
        self.findPaths(root.right, remaining - root.val, result, pathSoFar)
        del pathSoFar[len(pathSoFar) - 1]
            
