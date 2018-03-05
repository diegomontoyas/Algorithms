# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/sort-list/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        len = 0
        current = A
        while current is not None:
            len += 1
            current = current.next
 
        if len == 1: return A
 
        i=0
        current = A
        while i < len/2-2:
            i += 1
            current = current.next
        
        right = current.next
        current.next = None
        
        left = self.sortList(A)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def merge(self, A, B):
        head, b = ListNode("dummy"), ListNode("dummy")
        a = head
        a.next, b.next = A, B
    
        while a and b and a.next and b.next:
    
            if b.next.val < a.next.val:
                prevNextA = a.next
                thirdB = b.next.next
                
                a.next = b.next
                a.next.next = prevNextA
                b.next = thirdB
    
            a = a.next
    
        while a.next:
            a = a.next
            
        a.next = b.next
        return head.next
                
            
    
