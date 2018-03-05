# https://www.interviewbit.com/courses/programming/topics/graphs/problems/level-order/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        result = []
        queue = [A]
        nextLevelNodes = []
        level = []

        while queue:
            current = queue.pop(0)
            level.append(current.val)

            if current.left: nextLevelNodes.append(current.left)
            if current.right: nextLevelNodes.append(current.right)

            if not queue:
                result.append(level)
                level = []
                queue = nextLevelNodes
                nextLevelNodes = []

        return result
        
