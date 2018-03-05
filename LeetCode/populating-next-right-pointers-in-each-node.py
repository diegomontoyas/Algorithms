# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
# 92 ms

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        leftMost = root

        while leftMost:
            current = leftMost
            bridgeLeft = None

            while current:
                if current.left and current.right:
                    current.left.next = current.right

                bridgeLeft = (current.right or current.left) or bridgeLeft
                current = current.next

                if current:
                    bridgeRight = current.left or current.right

                    if bridgeLeft and bridgeRight:
                        bridgeLeft.next = bridgeRight

            current = leftMost
            leftMost = leftMost.left or leftMost.right

            while not leftMost and current:
                current = current.next

                if current:
                    leftMost = current.left or current.right

