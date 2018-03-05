# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/insertion-sort-list/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = ListNode("dummy")
        head.next = A
        
        befToSort = head
        toSort = head.next
        
        while toSort:
            last = head
            current = head.next
            
            while toSort is not current and current.val < toSort.val:
                last = current
                current = current.next

            continuationNode = toSort.next
            
            if toSort is not current:
                befToSort.next = toSort.next
                last.next = toSort
                toSort.next = current
            else:
                befToSort = toSort
            
            toSort = continuationNode
        
        return head.next
            
            
