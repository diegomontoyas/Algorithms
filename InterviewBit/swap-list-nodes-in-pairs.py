# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/swap-list-nodes-in-pairs/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        
        head = (A.next if A is not None else None) or A
        current = A
        previous = None
        
        while current is not None and current.next is not None:
            
            if previous is not None:
                previous.next = current.next
                    
            third = current.next.next
            current.next.next = current
            current.next = third
            previous = current
            current = third
            
        return head
                
                
