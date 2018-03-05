# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/subtract/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        
        #Find length
        length = 0
        current = A
        while current:
            length += 1
            current = current.next
            
        half = length/2
        
        #Find half
        i = 0
        current = A
        while i<half-1:
            current = current.next
            i += 1
        
        head = self.reverseBetween(A, half+1, length)

        firstHalfCurrent = head
        secondHalfCurrent = current.next
        
        i = 0
        while i<half:
            firstHalfCurrent.val = secondHalfCurrent.val - firstHalfCurrent.val
            
            firstHalfCurrent = firstHalfCurrent.next
            secondHalfCurrent = secondHalfCurrent.next
            i+=1
            
        head = self.reverseBetween(head, half+1, length)
        return head
        
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
        
        
        
            
