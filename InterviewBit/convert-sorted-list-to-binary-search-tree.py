# https://www.interviewbit.com/courses/programming/topics/graphs/problems/convert-sorted-list-to-binary-search-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if not A: return
        return self.addList(A, None)

    def addList(self, head, root):
        if not head: return root

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        current = head
        for i in xrange(length / 2-1):
            current = current.next

        beforeMiddle = current
        middle = current.next
        afterMiddle = middle.next if middle else None

        beforeMiddle.next = None

        if length == 1:
            middle = beforeMiddle

        root = self.add(middle.val if middle else None, root)
        root = self.addList(head if head is not middle else None, root)
        root = self.addList(afterMiddle, root)
        return root

    def add(self, elem, root):
        if elem is None: return root
        if root is None: return TreeNode(elem)

        current = root
        added = False
        while not added:
            if elem < current.val:
                if current.left is None:
                    current.left = TreeNode(elem)
                    added = True
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(elem)
                    added = True
                else:
                    current = current.right

        return root
        

