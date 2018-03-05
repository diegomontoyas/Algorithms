# https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/merge-two-sorted-lists/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        resultHead = ListNode("dummy")
        resultCurrent = resultHead
        
        currentA, currentB = A, B
        while currentA and currentB:
            if currentA.val < currentB.val:
                resultCurrent.next = currentA
                currentA = currentA.next
            else:
                resultCurrent.next = currentB
                currentB = currentB.next
                
            resultCurrent = resultCurrent.next
            
        if currentA:
            resultCurrent.next = currentA
        elif currentB:
            resultCurrent.next = currentB
            
        return resultHead.next
            
            
            
