# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/remove-duplicates-from-sorted-list-ii/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A is None: return None
        
        head = A
        last = head
        current = head.next
        nodeBeforeFirst = None

        while last is not None:
            
            if current is None or current.val != last.val:
                
                if nodeBeforeFirst is None and head is not last:
                    head = current

                elif nodeBeforeFirst is not None and nodeBeforeFirst.next is not last:
                    nodeBeforeFirst.next = current
                    
                else:
                    nodeBeforeFirst = last
                
            last = current
            if current is not None: current = current.next

        return head
                
                
        
        
