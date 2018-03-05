# https://www.interviewbit.com/courses/programming/topics/trees/problems/valid-binary-search-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return self.check(A)[0]
        
    def check(self, A):
        if not A:
            return True, None, None
            
        if not (A.left or A.right):
            return True, A.val, A.val
        
        valid, maxL, minL = self.check(A.left)
        if not valid or (maxL is not None and maxL >= A.val):
            return False, None, None

        valid, maxR, minR = self.check(A.right)
        if not valid or (minR is not None and minR <= A.val):
            return False, None, None
        
        maxVals = [v for v in [A.val, maxL, maxR] if v is not None]
        minVals = [v for v in [A.val, minL, minR] if v is not None]
        
        return True, max(maxVals), min(minVals)
        
        
