# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/reverse-link-list-ii/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n: return A
        head = ListNode("dummy")
        head.next = A

        beforeStart = head
        i = 1
        while i < m:
            beforeStart = beforeStart.next
            i += 1
        i += 1
        
        start = beforeStart.next
        prev = start
        current = prev.next
        
        while i <= n:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i+=1
        
        beforeStart.next = prev
        start.next = current
        return head.next
        
        
