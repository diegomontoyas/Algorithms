# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/unique-binary-search-trees/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        return self.genTrees(1, A)
        
    def genTrees(self, min, max):
        if max < min: return [None]
        if max == min: return [TreeNode(min)]
        result = []
        
        for n in xrange(min, max+1):
            import itertools
            leftChildren = self.genTrees(min, n-1)
            rightChildren = self.genTrees(n+1, max)
            
            for child1, child2 in list(itertools.product(leftChildren, rightChildren)):
                root = TreeNode(n)
            
                if (child1 and child1.val < n) or (child2 and child2.val > n):
                    root.left = child1
                    root.right = child2
                else:
                    root.left = child2
                    root.right = child1
            
                result.append(root)
            
        return result
            
