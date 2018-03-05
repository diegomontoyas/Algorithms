# https://www.interviewbit.com/courses/programming/topics/hashing/problems/copy-list/
# 

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        copiedNodes = {}
        
        copiedHead = RandomListNode("dummy")
        copiedCurrent = copiedHead
        
        toCopy = head
        while toCopy:
            newCopy = RandomListNode(toCopy.label)
            copiedCurrent.next = newCopy
            copiedNodes[newCopy.label] = newCopy
            
            toCopy = toCopy.next
            copiedCurrent = copiedCurrent.next
        
        current = head
        while current:
            if current.random:
                copiedNodes[current.label].random = copiedNodes[current.random.label]
            current = current.next
            
        return copiedHead.next
            
