# https://www.interviewbit.com/courses/programming/topics/trees/problems/zigzag-level-order-traversal-bt/
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
    def zigzagLevelOrder(self, A):
        result = [[A.val]] if A else []
        queue = [A] if A else []
        level = 0
        
        while queue:
            newQueue = []
            
            for node in queue:
                if node.left: newQueue.append(node.left)
                if node.right: newQueue.append(node.right)
        
            if newQueue:
                nodes = reversed(newQueue) if level % 2 == 0 else newQueue
                result.append([node.val for node in nodes])
                
            queue = newQueue
            level += 1
        
        return result
        
