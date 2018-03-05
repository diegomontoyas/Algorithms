# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/list-cycle/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A is None: return
        
        dummy = ListNode("dummy")
        current = A
        while current.next is not dummy:
            next = current.next
            if next is None: return
            current.next = dummy
            current = next
            
        return current
            
