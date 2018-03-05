// https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/remove-duplicates-from-sorted-list/
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
    public ListNode deleteDuplicates(ListNode a) {
        
        ListNode current = a, last = null;
        
        while (current != null) {
            if (last != null && last.val == current.val) {
                ListNode next = current.next;
                last.next = next;
            } else {
                last = current;
            }
            
            current = current.next;
        }
        
        return a;
    }
}

