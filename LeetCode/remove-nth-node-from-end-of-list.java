// https://leetcode.com/problems/remove-nth-node-from-end-of-list
// 16 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        
        int i=0;
        ListNode leader = head;
        
        while(leader != null && i<n) {
            i++;
            leader = leader.next;
        }
        
        if(leader == null) {
            return head.next;
        } else {
            ListNode beforeNth = head;
            while(leader.next != null) {
                leader = leader.next;
                beforeNth = beforeNth.next;
            }
            
            beforeNth.next = beforeNth.next.next;
        }
        
        return head;
    }
}
