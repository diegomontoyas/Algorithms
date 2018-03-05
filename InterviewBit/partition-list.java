// https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/partition-list/
// 

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode partition(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode current = dummy;
        ListNode leftPartitionCurrent = dummy;
        
        while (current.next != null) {
            ListNode next = current.next;
            
            if (current.next.val < n) {
                move(leftPartitionCurrent, current);
                leftPartitionCurrent = leftPartitionCurrent.next;
            }
            
            current = next;
        }
        
        return dummy.next;
    }
    
    private void move(ListNode after, ListNode nodeBefore) {
       
        // Disconnect
        ListNode toMove = nodeBefore.next;
        nodeBefore.next = toMove.next;
        
        // Connect
        toMove.next = after.next;
        after.next = toMove;
    }
}

