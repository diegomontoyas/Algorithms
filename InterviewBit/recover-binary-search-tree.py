# https://www.interviewbit.com/courses/programming/topics/trees/problems/recover-binary-search-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        badPairs = self._findSwapped(A)
        
        if len(badPairs) == 1:
            return sorted(list(badPairs[0]))
        else:
            return sorted([badPairs[0][0], badPairs[1][1]])
    
    def _findSwapped(self, root):
        badPairs = []
        last = [float("-inf")]
        current = root 
        
        def process(new):
            if new < last[0]:
                badPairs.append((last[0], new))
            last[0] = new
         
        while current:
            if not current.left:
                process(current.val)
                current = current.right
            else:
                node = current.left
                while node.right and node.right is not current:
                    node = node.right
      
                if not node.right:
                    node.right = current
                    current = current.left
                else:
                    node.right = None
                    process(current.val)
                    current = current.right
                    
        return badPairs

